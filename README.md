# Resume Analyser

This is a web application built with Streamlit that helps users analyze their resumes, providing insights on skills, course recommendations, and tips for improving the resume. The application extracts information from uploaded resumes in PDF format using `pyresparser` and performs analysis based on the extracted data.

## Features

- **Resume Analysis**: The application extracts basic information from the uploaded resume, including name, email, contact, and number of pages. It then provides an analysis of the resume content.
- **Skills Recommendation**: Based on the skills mentioned in the resume, the application recommends additional skills that can enhance the user's profile. It provides recommended skills for various fields such as Data Science, Web Development, Android Development, iOS Development, and UI-UX Development.
- **Courses & Certificates Recommendations**: The application suggests relevant courses and certificates based on the recommended skills for each field using finetuned nous-hermes2 Model from Gradient. Users can explore these courses to further enhance their skills and qualifications.
- **Resume Tips & Ideas**: The application evaluates the resume content and provides tips and ideas for improvement. It suggests adding sections like Objective, Declaration, Hobbies/Interests, Achievements, and Projects to enhance the overall quality of the resume.
- **Resume Score**: The application calculates a resume writing score based on the content added to the resume. It provides visual feedback on the score and encourages users to improve their resumes accordingly.

## Screenshot:
<img src="https://github.com/chaitanya1705/CodeCraft-Byte_brawlers-Resume_Analyser/blob/main/Resume-Analyzer%20(2).png">

## Installation

**NOTE**:**USE PYTHON VERSION 3.10 FOR BEST RESULTS**

1. Clone the repository:

```bash
git clone https://github.com/irondis76/AI-Resume-Analyzer
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Finetune Model Using gradient.ai 

```bash
python finetune.py
```

4.Create New Directory `Uploaded_Resumes` is created with a resume in it.

```bash
mkdir Uploaded_Resumes
```

5. Run the application:

```bash
streamlit run app.py
```

## Usage

1. Upload your resume in PDF format.
2. The application will analyze the content and provide insights on your skills, course recommendations, and tips for improving your resume.
3. Explore the recommended skills and courses to enhance your qualifications.
4. Follow the resume tips and ideas to improve the overall quality of your resume.
5. Check your resume score to see how well it is written and make necessary adjustments.



## License

This project is licensed under the [MIT License](LICENSE).
