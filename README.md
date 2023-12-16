# CS 466 Final Project: Sequence Aligner

## Team Members:
- Pooja Ganesh (pganesh4, pganesh4@illinois.edu)
- Dirgh Shah (dirghvs2, dirghvs2@illinois.edu)
- Purvansh Bal (pbal3, pbal3@illinois.edu)

## Brief Motivation:
Welcome to our CS 466 Final Project! Our team is excited to introduce an interactive web platform focused on implementing and visualizing a range of sequence alignment algorithms. This project encompasses Global Alignment, Local Alignment, Fitting Alignment, Gap Affine Penalty Alignment, and Multiple Sequence Alignment for DNA, RNA, and protein sequences.

## Planned Method/Experimentations:
We plan to implement algorithms covered in class, incorporating standard visualization techniques such as the matrix representation used in our reference aligner. Our project is built in Python, utilizing the Django framework for web development. Additionally, we leverage standard Python libraries like NumPy, Pandas, and Matplotlib for efficient visualization.

### Week 1 (November 17 - November 24):
- Set up the development environment and version control.
- Design the user interface and plan implementation details.
- Implement Global, Local, and Fitting Alignment algorithms.

### Week 2 (November 25 - December 2):
- Implement Gap Affine Penalty Alignment Algorithm.
- Make improvements to the frontend and introduce additional features.

### Week 3 (December 3 - December 10):
- Develop visualization features for all alignment algorithms.
- Initiate work on Multiple Sequence Alignment.

### Week 4 (December 11 - December 15):
- Complete the implementation of the MSA algorithm and integrate it into the tool.
- Conduct debugging and refactoring of the codebase to ensure deployment readiness.
- Work on the Project Report.

We ensure effective collaboration through regular meetings, hack sessions, and version control via our GitHub repository.

## How to Run:
To run the Sequence Aligner locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Purvanshbal/Sequence_Aligner.git
   cd Sequence_Aligner

2. **Install Required Dependencies**
    You will need to install the libraries used for this project: namely flask and numpy. You can do that using:
    pip install <library-name>. If your local system doesn't support these libraries, you should consider creating a
    virtual environment

3. **Run the WebApp**
    From the Sequence_Aligner repo, open the terminal and run the command "python run.py" or "python3 run.py"

4. **Accessing the UI**
    Open your web browser and go to http://localhost:8000.

    Now you can explore the Sequence Aligner and interact with the implemented algorithms.