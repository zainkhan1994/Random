import os

def main():
    # File path (no need to modify)
    file_path = "/System/Volumes/Data/Users/zainkhan/Projects/Deployment /Personal/Google Calendar/events.txt"

    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' not found. Ensure the file exists.")
            return

        # Read the file content
        with open(file_path, 'r') as file:
            content = file.readlines()

        # Generate a report with a clean visualization
        print("\n" + "="*40)
        print("Google Calendar Events Analysis")
        print("="*40)
        print(f"File Path: {file_path}")
        print(f"Total Number of Lines: {len(content)}")
        print("\n--- Preview of First 10 Lines ---")
        for i, line in enumerate(content[:10], start=1):
            print(f"{i:>2}: {line.strip()}")

        # Analyzing for dates
        print("\n--- Analysis ---")
        date_lines = [line for line in content if 'DATE:' in line.upper()]
        print(f"Number of Lines Containing 'DATE:': {len(date_lines)}")

        if date_lines:
            print("\n--- Sample Dates ---")
            for i, line in enumerate(date_lines[:5], start=1):
                print(f"{i}: {line.strip()}")

        # Visual separator
        print("\n" + "="*40)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()