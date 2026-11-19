[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/57NVG7ol)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=19824833)
# MSE 641 - Clickbait Detection Challenge: Baseline Scripts

This repository contains naive baseline scripts for the MSE 641 Clickbait Detection Challenge Milestone (Default Project). The baseline implementations provide a starting point for both Task 1 (spoiler type classification) and Task 2 (spoiler generation).

## Repository Structure

```
├── README.md
├── requirements.txt
├── data/
│   ├── test.jsonl
│   ├── train.jsonl
│   └── val.jsonl
├── Task_1/
│   ├── naive_baseline_task1.py
│   └── convert_task1_to_csv.py
└── Task_2/
    ├── naive_baseline_task2.py
    └── convert_task2_to_csv.py
```

## Quick Start

### 1. Set Up Virtual Environment (if not using Codespaces)

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Task 1 (Spoiler Type Classification)

```bash
# Navigate to Task 1 directory
cd Task_1

# Run the baseline
python3 naive_baseline_task1.py --input ../data/test.jsonl --output task1_results.jsonl

# Convert to CSV for Kaggle submission
python3 convert_task1_to_csv.py

# Check the output
head -5 task1_submission.csv
```

### 3. Run Task 2 (Spoiler Generation)

```bash
# Navigate to Task 2 directory
cd ../Task_2

# Run the baseline
python3 naive_baseline_task2.py --input ../data/test.jsonl --output task2_results.jsonl

# Convert to CSV for Kaggle submission
python3 convert_task2_to_csv.py

# Check the output
head -5 task2_submission.csv
```

## Task Descriptions

### Task 1: Spoiler Type Classification
**Goal**: Classify what type of spoiler is needed for each clickbait post.

**Output Types**:
- `phrase` - Short phrase spoiler
- `passage` - Longer passage spoiler  
- `multi` - Multiple non-consecutive pieces of text

**Baseline Strategy**: The naive baseline predicts `"passage"` for all clickbait posts.

**Expected Output Format**:
```csv
id,spoilerType
0,passage
1,passage
2,passage
```

### Task 2: Spoiler Generation
**Goal**: Generate text that "spoils" the clickbait by revealing what the linked article is actually about.

**Baseline Strategy**: The naive baseline uses the title of the linked webpage (`targetTitle`) as the spoiler text.

**Expected Output Format**:
```csv
id,spoiler
0,"All the scenes are actually in the movie"
1,"4.47 billion years ago"
```

## Data Format

The input data (`test.jsonl`, `train.jsonl`, `val.jsonl`) contains JSON objects with the following key fields:

- `id`: Unique identifier for each post
- `postText`: The clickbait post text
- `targetTitle`: Title of the linked webpage
- `targetParagraphs`: Main content paragraphs from the linked page
- `targetUrl`: URL of the linked webpage

**Training/Validation data also includes**:
- `tags`: Ground truth spoiler type (`"phrase"`, `"passage"`, or `"multi"`)
- `spoiler`: Human-extracted spoiler text
- `humanSpoiler`: Human-generated spoiler text

## Kaggle Submission Instructions

### Step 1: Access Your Competition
1. Go to the Kaggle competition page for Task 1 (https://www.kaggle.com/competitions/task-1-clickbait-detection-msci-641-s-25) or Task 2 (https://www.kaggle.com/competitions/task-2-clickbait-detection-msci-641-s-25)
2. Make sure you're logged into Kaggle and have joined the competition

### Step 2: Submit Your CSV
1. Click the **"Submit Predictions"** button in the top right corner of the website
2. Upload your CSV file:
   - For Task 1: `task1_submission.csv`
   - For Task 2: `task2_submission.csv`
3. Add a submission description (e.g., "Milestone submission - naive baseline")
4. Click **"Make Submission"**

### Step 3: Verify Submission
1. Check the **"My Submissions"** tab to see your submission status
2. Look for a green checkmark indicating successful submission
3. Note your score for the final project report

### Step 4: Upload a one-page PDF document to Milestone Dropbox on Learn
Your PDF should specify:
- Your name(s) and student ID(s)
- The Kaggle username under which the submissions were made
- Submission scores for both tasks
- Date of submission
- Name of submitted files

