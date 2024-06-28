#User can use the create_Files.sh [Day] to run this file

PROJECT_DIR="C:\Users\syeda\Downloads\Personal\Python Project\Advent of Code"
DAY=$1
FOLDER_NAME="$PROJECT_DIR\Day $DAY"
PART1_FILE_NAME="$FOLDER_NAME\Part 1.py"
PART2_FILE_NAME="$FOLDER_NAME\Part 2.py"
INPUT_FILE_NAME="$FOLDER_NAME\input.txt"
TESTINPUT_FILE_NAME="$FOLDER_NAME\inputTest.txt"

mkdir -p "$FOLDER_NAME"
touch "$PART1_FILE_NAME"
touch "$PART2_FILE_NAME"
touch "$INPUT_FILE_NAME"
touch "$TESTINPUT_FILE_NAME"