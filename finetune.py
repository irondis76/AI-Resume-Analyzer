from gradientai import Gradient
import os

os.environ["GRADIENT_ACCESS_TOKEN"]="<YOUR API KEY>"
os.environ["GRADIENT_WORKSPACE_ID"]="<YOUR WORKSPACE ID>"

samples = [
    {"inputs": "### Instruction: What is the best course for machine learning? \n\n### Response: Some popular machine learning courses include 'Machine Learning Crash Course by Google', 'Machine Learning A-Z by Udemy', and 'Machine Learning by Andrew NG'."},
    {"inputs": "### Instruction: Give me a course for learning data science with Python. \n\n### Response: You can consider 'Data Scientist with Python' by DataCamp or 'Programming for Data Science with Python' by Udacity."},
    {"inputs": "### Instruction: Which course is recommended for becoming a full stack web developer? \n\n### Response: 'Full Stack Web Developer by Udacity' or 'Full Stack Web Developer - MEAN Stack' are popular choices for full stack web development."},
    {"inputs": "### Instruction: Suggest a course for Android app development using Kotlin. \n\n### Response: 'Android App Development Masterclass using Kotlin' and 'Become an Android Kotlin Developer by Udacity' are good options for learning Android app development with Kotlin."},
    {"inputs": "### Instruction: What are some courses for iOS app development? \n\n### Response: You might want to check out 'iOS App Development by LinkedIn' and 'iOS & Swift - The Complete iOS App Development Bootcamp'."},
    {"inputs": "### Instruction: I'm interested in learning UX/UI design. Any recommended courses? \n\n### Response: Consider courses like 'Google UX Design Professional Certificate' and 'UI / UX Design Specialization' for UX/UI design."},
    {"inputs":
        "### Instruction: Give me a course for learning ReactJS. \n\n### Response: You can take the 'ReactJS Project Development Training' or 'React Crash Course [Free]'."},
    {"inputs": "### Instruction: I want to learn about Flask for web development. Any courses available? \n\n### Response: 'Flask: Develop Web Applications in Python' is a good course for learning Flask."},
    {"inputs":
        "### Instruction: What courses are available for learning Android app development? \n\n### Response: There are various courses available such as 'Android Development for Beginners [Free]', 'Android App Development Specialization', and 'The Complete Android Developer Course'."},
    {"inputs":
        "### Instruction: Which course should I take to learn Swift programming? \n\n### Response: Consider 'Swift Tutorial - Full Course for Beginners [Free]' or 'Learn Swift by Codecademy' for learning Swift programming."},
    {"inputs": "### Instruction: Can you suggest a course for data science foundations? \n\n### Response: You might find 'Data Science Foundations: Fundamentals by LinkedIn' helpful for learning data science foundations."},
    {"inputs": "### Instruction: Give me a course to become a front end web developer. \n\n### Response: 'Front End Web Developer by Udacity' is a good course for becoming a front end web developer."},
    {"inputs": "### Instruction: Which course is best for learning UX design? \n\n### Response: 'Become a UX Designer by Udacity' is a recommended course for learning UX design."},
    {"inputs": "### Instruction: What is the recommended course for learning machine learning with TensorFlow? \n\n### Response: 'Intro to Machine Learning with TensorFlow' by Udacity is a good course for learning machine learning with TensorFlow."},
    {"inputs": "### Instruction: I want to learn Android app development. Which course should I take? \n\n### Response: Consider taking 'Android Basics by Google' or 'Associate Android Developer Certification' for Android app development."},
    {"inputs": "### Instruction: Suggest a course for Python and Django full stack web development. \n\n### Response: You might want to check out 'Python and Django Full Stack Web Developer Bootcamp' for Python and Django full stack web development."},
    {"inputs":
        "### Instruction: What courses are available for data scientists? \n\n### Response: There are several courses available such as 'Data Scientist Master Program of Simplilearn (IBM)' and 'Data Scientist with Python'."},
    {"inputs": "### Instruction: Give me a course to learn iOS app development with Swift. \n\n### Response: Consider 'iOS App Development with Swift Specialization' for learning iOS app development with Swift."},
    {"inputs": "### Instruction: Which course is recommended for learning R programming for data science? \n\n### Response: 'Programming for Data Science with R' by Udacity is a good course for learning R programming for data science."},
    {"inputs":
        "### Instruction: What are some courses for learning web development with Node.js? \n\n### Response: You can consider 'Node.js and Express.js [Free]' for learning web development with Node.js."},
    {"inputs": "### Instruction: I'm interested in learning Flutter app development. Any recommended courses? \n\n### Response: Consider courses like 'Flutter & Dart - The Complete Flutter App Development Course' for learning Flutter app development."},
    {"inputs": "### Instruction: Give me a course for developing full stack web applications with MEAN Stack. \n\n### Response: 'Full Stack Web Developer - MEAN Stack' is a good course for developing full stack web applications with MEAN Stack."},
    {"inputs": "### Instruction: What courses are available for learning data science? \n\n### Response: You might find courses like 'Introduction to Data Science' and 'Data Science Foundations: Fundamentals by LinkedIn' helpful for learning data science."},
    {"inputs":
        "### Instruction: Which course is best for learning Android app development? \n\n### Response: Consider courses like 'The Complete Android Developer Course' and 'Android Development for Beginners [Free]' for learning Android app development."},
    {"inputs": "### Instruction: Suggest a course for becoming a machine learning engineer. \n\n### Response: Consider courses like 'Machine Learning by Andrew NG' and 'Machine Learning Crash Course by Google' for becoming a machine learning engineer."},
    {"inputs": "### Instruction: Give me a course for learning front end web development. \n\n### Response: 'Front End Web Developer by Udacity' is a recommended course for learning front end web development."},
    {"inputs":
        "### Instruction: What courses are available for learning React? \n\n### Response: 'ReactJS Project Development Training' and 'React Crash Course [Free]' are popular courses for learning React."},
    {"inputs": "### Instruction: Which course should I take to learn Python for data science? \n\n### Response: Consider 'Data Scientist with Python' for learning Python for data science."},
    {"inputs": "### Instruction: I want to learn about iOS app development. Any recommended courses? \n\n### Response: 'iOS & Swift - The Complete iOS App Development Bootcamp' is a good course for learning about iOS app development."},
    {"inputs": "### Instruction: Can you suggest a course for web development using Flask? \n\n### Response: 'Flask: Develop Web Applications in Python' is a recommended course for web development using Flask."},
    {"inputs": "### Instruction: Give me a course for Android app development with Kotlin. \n\n### Response: Consider 'Android App Development Masterclass using Kotlin' for Android app development with Kotlin."},
    {"inputs":
        "### Instruction: What courses are available for learning Swift programming? \n\n### Response: You can consider courses like 'Swift Tutorial - Full Course for Beginners [Free]' for learning Swift programming."},
    {"inputs": "### Instruction: Which course is best for learning data science fundamentals? \n\n### Response: 'Data Science Foundations: Fundamentals by LinkedIn' is a good course for learning data science fundamentals."},
    {"inputs": "### Instruction: Suggest a course for becoming a full stack web developer. \n\n### Response: 'Full Stack Web Developer by Udacity' or 'Full Stack Web Developer - MEAN Stack' are popular choices for becoming a full stack web developer."},
    {"inputs": "### Instruction: Give me a course to learn Android app development. \n\n### Response: Consider 'Android Basics by Google' or 'Associate Android Developer Certification' for learning Android app development."},
    {"inputs": "### Instruction: What are some courses for Python and Django full stack web development? \n\n### Response: You might want to check out 'Python and Django Full Stack Web Developer Bootcamp' for Python and Django full stack web development."},
    {"inputs": "### Instruction: Which course is recommended for becoming a front end web developer? \n\n### Response: 'Front End Web Developer by Udacity' is a recommended course for becoming a front end web developer."},
    {"inputs": "### Instruction: What courses are available for learning UX/UI design? \n\n### Response: Consider courses like 'Google UX Design Professional Certificate' and 'UI / UX Design Specialization' for learning UX/UI design."},
    {"inputs":
        "### Instruction: Give me a course for learning ReactJS. \n\n### Response: You can take the 'ReactJS Project Development Training' or 'React Crash Course [Free]'."},
    {"inputs": "### Instruction: I want to learn about Flask for web development. Any courses available? \n\n### Response: 'Flask: Develop Web Applications in Python' is a good course for learning Flask."},
    {"inputs":
        "### Instruction: What courses are available for learning Android app development? \n\n### Response: There are various courses available such as 'Android Development for Beginners [Free]', 'Android App Development Specialization', and 'The Complete Android Developer Course'."},
    {"inputs":
        "### Instruction: Which course should I take to learn Swift programming? \n\n### Response: Consider 'Swift Tutorial - Full Course for Beginners [Free]' or 'Learn Swift by Codecademy' for learning Swift programming."},
    {"inputs": "### Instruction: Can you suggest a course for data science foundations? \n\n### Response: You might find 'Data Science Foundations: Fundamentals by LinkedIn' helpful for learning data science foundations."},
    {"inputs": "### Instruction: Give me a course to become a front end web developer. \n\n### Response: 'Front End Web Developer by Udacity' is a good course for becoming a front end web developer."},
    {"inputs": "### Instruction: Which course is best for learning UX design? \n\n### Response: 'Become a UX Designer by Udacity' is a recommended course for learning UX design."},
    {"inputs": "### Instruction: What is the recommended course for learning machine learning with TensorFlow? \n\n### Response: 'Intro to Machine Learning with TensorFlow' by Udacity is a good course for learning machine learning with TensorFlow."},
    {"inputs": "### Instruction: I want to learn Android app development. Which course should I take? \n\n### Response: Consider taking 'Android Basics by Google' or 'Associate Android Developer Certification' for Android app development."},
    {"inputs": "### Instruction: Suggest a course for Python and Django full stack web development. \n\n### Response: You might want to check out 'Python and Django Full Stack Web Developer Bootcamp' for Python and Django full stack web development."},
    {"inputs":
        "### Instruction: What courses are available for data scientists? \n\n### Response: There are several courses available such as 'Data Scientist Master Program of Simplilearn (IBM)' and 'Data Scientist with Python'."},
    {"inputs": "### Instruction: Give me a course to learn iOS app development with Swift. \n\n### Response: Consider 'iOS App Development with Swift Specialization' for learning iOS app development with Swift."},
    {"inputs": "### Instruction: Which course is recommended for learning R programming for data science? \n\n### Response: 'Programming for Data Science with R' by Udacity is a good course for learning R programming for data science."},
    {"inputs":
        "### Instruction: What are some courses for learning web development with Node.js? \n\n### Response: You can consider 'Node.js and Express.js [Free]' for learning web development with Node.js."},
    {"inputs": "### Instruction: I'm interested in learning Flutter app development. Any recommended courses? \n\n### Response: Consider courses like 'Flutter & Dart - The Complete Flutter App Development Course' for learning Flutter app development."},
    {"inputs": "### Instruction: Give me a course for developing full stack web applications with MEAN Stack. \n\n### Response: 'Full Stack Web Developer - MEAN Stack' is a good course for developing full stack web applications with MEAN Stack."},
    {"inputs": "### Instruction: What courses are available for learning data science? \n\n### Response: You might find courses like 'Introduction to Data Science' and 'Data Science Foundations: Fundamentals by LinkedIn' helpful for learning data science."},
    {"inputs":
        "### Instruction: Which course is best for learning Android app development? \n\n### Response: Consider courses like 'The Complete Android Developer Course' and 'Android Development for Beginners [Free]' for learning Android app development."},
    {"inputs": "### Instruction: Suggest a course for becoming a machine learning engineer. \n\n### Response: Consider courses like 'Machine Learning by Andrew NG' and 'Machine Learning Crash Course by Google' for becoming a machine learning engineer."},
    {"inputs": "### Instruction: Give me a course for learning front end web development. \n\n### Response: 'Front End Web Developer by Udacity' is a recommended course for learning front end web development."},
    {"inputs":
        "### Instruction: What courses are available for learning React? \n\n### Response: 'ReactJS Project Development Training' and 'React Crash Course [Free]' are popular courses for learning React."},
    {"inputs": "### Instruction: Which course should I take to learn Python for data science? \n\n### Response: Consider 'Data Scientist with Python' for learning Python for data science."},
    {"inputs": "### Instruction: I want to learn about iOS app development. Any recommended courses? \n\n### Response: 'iOS & Swift - The Complete iOS App Development Bootcamp' is a good course for learning about iOS app development."},
    {"inputs": "### Instruction: Can you suggest a course for web development using Flask? \n\n### Response: 'Flask: Develop Web Applications in Python' is a recommended course for web development using Flask."},
    {"inputs": "### Instruction: Give me a course for Android app development with Kotlin. \n\n### Response: Consider 'Android App Development Masterclass using Kotlin' for Android app development with Kotlin."},
    {"inputs":
        "### Instruction: What courses are available for learning Swift programming? \n\n### Response: You can consider courses like 'Swift Tutorial - Full Course for Beginners [Free]' for learning Swift programming."},
    {"inputs": "### Instruction: Which course is best for learning data science fundamentals? \n\n### Response: 'Data Science Foundations: Fundamentals by LinkedIn' is a good course for learning data science fundamentals."},
    {"inputs": "### Instruction: Suggest a course for becoming a full stack web developer. \n\n### Response: 'Full Stack Web Developer by Udacity' or 'Full Stack Web Developer - MEAN Stack' are popular choices for becoming a full stack web developer."},
    {"inputs": "### Instruction: Give me a course to learn Android app development. \n\n### Response: Consider 'Android Basics by Google' or 'Associate Android Developer Certification' for learning Android app development."},
    {"inputs": "### Instruction: What are some courses for Python and Django full stack web development? \n\n### Response: You might want to check out 'Python and Django Full Stack Web Developer Bootcamp' for Python and Django full stack web development."},
    {"inputs": "### Instruction: Which course is recommended for becoming a front end web developer? \n\n### Response: 'Front End Web Developer by Udacity' is a recommended course for becoming a front end web developer."},
    {"inputs": "### Instruction: What courses are available for learning UX/UI design? \n\n### Response: Consider courses like 'Google UX Design Professional Certificate' and 'UI / UX Design Specialization' for learning UX/UI design."},
    {"inputs":
        "### Instruction: Give me a course for learning ReactJS. \n\n### Response: You can take the 'ReactJS Project Development Training' or 'React Crash Course [Free]'."},
    {"inputs": "### Instruction: I want to learn about Flask for web development. Any courses available? \n\n### Response: 'Flask: Develop Web Applications in Python' is a good course for learning Flask."},
    {"inputs":
        "### Instruction: What courses are available for learning Android app development? \n\n### Response: There are various courses available such as 'Android Development for Beginners [Free]', 'Android App Development Specialization', and 'The Complete Android Developer Course'."},
    {"inputs":
        "### Instruction: Which course should I take to learn Swift programming? \n\n### Response: Consider 'Swift Tutorial - Full Course for Beginners [Free]' or 'Learn Swift by Codecademy' for learning Swift programming."},
    {"inputs": "### Instruction: Can you suggest a course for data science foundations? \n\n### Response: You might find 'Data Science Foundations: Fundamentals by LinkedIn' helpful for learning data science foundations."},
    {"inputs": "### Instruction: Give me a course to become a front end web developer. \n\n### Response: 'Front End Web Developer by Udacity' is a good course for becoming a front end web developer."},
]

with Gradient() as gradient:
      base_model = gradient.get_base_model(base_model_slug="nous-hermes2")

      new_model_adapter = base_model.create_model_adapter(
          name="Course_Recommender_Model"
      )
      query="Give me a course to become a front end web developer."
      print(f"Created model adapter with id {new_model_adapter.id}")
      sample_query = f"### Instruction: {query} \n\n### Response:"
      print(f"Asking: {sample_query}")

      # before fine-tuning
      completion = new_model_adapter.complete(query=sample_query, max_generated_token_count=200).generated_output
      print(f"Generated (before fine-tune): {completion}")


      num_epochs = 3
      count = 0
      while count < num_epochs:
          print(f"Fine-tuning the model, iteration {count + 1}")
          new_model_adapter.fine_tune(samples=samples)
          count = count + 1

      # after fine-tuning
      completion = new_model_adapter.complete(query=sample_query, max_generated_token_count=100).generated_output
      print(f"Generated (after fine-tune): {completion}")

