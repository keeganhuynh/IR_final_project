# IR_final_project

**Support request**
1. (27/01/2024) I don't know how to use the CIRR dataset to evaluate other similarity measures because I haven't read the dataset structure. If you have time on your hands, please check the dataset structure and provide an explanation for us.
![image](https://github.com/keeganhuynh/IR_final_project/assets/58461941/79a9d0f9-ed58-4537-a081-e78af92cd282)

2. Hiệp is coding to evaluate using Recall in test1 


**Problem:**
1. The paper code relies on multi-threading for acceleration, but due to the original code being over 4 years old, there might be environmental conflicts. The code still runs, but after completion, it reports a multi-threading error.
2. I have corrected the file paths and some syntax in the old Python version that is not compatible with version 3.10.
3. I have set args.distributed to False by default (because I cannot perform computations on multiple GPUs)

**Read carefully GIT IGNORE and add folder DATA with exactly structure:**

![image](https://github.com/keeganhuynh/IR_final_project/assets/58461941/aec96078-360b-4b0d-8baf-5c3ae57ecce8)


**TESTING CIRR (data: test1, test2)**
-> https://cirr.cecs.anu.edu.au/


