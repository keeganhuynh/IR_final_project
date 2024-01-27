# IR_final_project

**Problem:**
1. The paper code relies on multi-threading for acceleration, but due to the original code being over 4 years old, there might be environmental conflicts. The code still runs, but after completion, it reports a multi-threading error.
2. I have corrected the file paths and some syntax in the old Python version that is not compatible with version 3.10.
3. 3. I have set args.distributed to False by default (because I cannot perform computations on multiple GPUs)

**Read carefully GIT IGNORE and add folder DATA with exactly structure:**
cirr
  ├── captions
        └──cap.rc2.val.json
  ├── dev
  └── image_splits
        └──split.rc2.val.json

**TESTING CIRR (data: test1, test2) -> https://cirr.cecs.anu.edu.au/


