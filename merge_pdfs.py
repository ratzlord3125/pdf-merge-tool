import os
from PyPDF2 import PdfMerger
from tqdm import tqdm

def list_pdf_files(folder_path):
    files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    return sorted(files)

def show_file_list(files):
    print("\n📄 PDF Files:")
    for idx, file in enumerate(files):
        print(f"{idx + 1}. {file}")

def edit_pdf_list(files):
    while True:
        show_file_list(files)
        print("\nOptions:")
        print("1. Remove a file")
        print("2. Change file order")
        print("3. Continue to merge")
        choice = input("Choose an option (1-3): ").strip()

        if choice == '1':
            try:
                idx = int(input("Enter the index of the file to remove: ")) - 1
                if 0 <= idx < len(files):
                    removed = files.pop(idx)
                    print(f"✅ Removed: {removed}")
                else:
                    print("❌ Invalid index.")
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == '2':
            try:
                print("\nEnter the new order as space-separated indices (e.g., 3 1 2):")
                new_order = list(map(int, input("> ").strip().split()))
                if sorted(new_order) != list(range(1, len(files) + 1)):
                    print("❌ Invalid order. Must use each index exactly once.")
                    continue
                files = [files[i - 1] for i in new_order]
                print("✅ Order updated.")
            except Exception:
                print("❌ Error updating order. Please try again.")
        elif choice == '3':
            break
        else:
            print("❌ Invalid choice.")
    return files

def merge_pdfs(input_folder, output_file, ordered_files):
    merger = PdfMerger()
    total_files = len(ordered_files)

    print(f"\n📦 Merging {total_files} PDF files...")
    with tqdm(total=total_files, desc="Progress", unit="file") as pbar:
        for file in ordered_files:
            full_path = os.path.join(input_folder, file)
            try:
                merger.append(full_path)
            except Exception as e:
                print(f"❌ Error processing {file}: {e}")
            pbar.update(1)

    try:
        merger.write(output_file)
        print(f"\n✅ Merge complete. Output saved to: {output_file}")
    except Exception as e:
        print(f"❌ Failed to write output PDF: {e}")
    finally:
        merger.close()

def main_menu():
    print("\n📝 PDF Merger - Menu")
    print("---------------------")
    print("1. Merge PDF files in a folder")
    print("2. Exit")
    
    choice = input("Enter your choice: ").strip()
    if choice == '1':
        folder = input("\nEnter full path to folder containing PDF files: ").strip('" ')
        if not os.path.isdir(folder):
            print("❌ Folder not found.")
            return

        output = input("Enter output PDF file path (e.g., merged_output.pdf): ").strip('" ')
        if not output.lower().endswith(".pdf"):
            output += ".pdf"

        files = list_pdf_files(folder)
        if not files:
            print("❌ No PDF files found in the folder.")
            return

        files = edit_pdf_list(files)
        merge_pdfs(folder, output, files)

    elif choice == '2':
        print("👋 Exiting...")
    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main_menu()
