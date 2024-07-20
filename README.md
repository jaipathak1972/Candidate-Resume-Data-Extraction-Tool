![image](https://github.com/user-attachments/assets/ce0b11f6-77cc-407f-b443-28688492ecc3)

<h1>ATS Resume Expert</h1>

<p>Welcome to <strong>ATS Resume Expert</strong>, an advanced tool for extracting and analyzing resume data using Google Generative AI and Streamlit. This project leverages Google Gemini and PDF2Image to extract critical information from resumes, providing valuable insights into job applicants' skills, experience, and more.</p>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#setup">Setup</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#prompts">Prompts</a></li>
</ul>

<h2 id="introduction">Introduction</h2>
<p><strong>ATS Resume Expert</strong> is designed to help you analyze resumes efficiently using the power of Google Generative AI. This tool can extract various details from resumes such as technical skills, candidate name, location, and total experience.</p>

<h2 id="features">Features</h2>
<ul>
    <li>Extracts technical skills from resumes</li>
    <li>Extracts candidate name</li>
    <li>Extracts candidate location</li>
    <li>Extracts total experience in numerical value</li>
</ul>

<h2 id="setup">Setup</h2>
<p>To get started with the project, follow these steps:</p>
<ol>
    <li><strong>Clone the repository:</strong>
        <pre><code>git clone https://github.com/your-username/ATS-Resume-Expert.git
cd ATS-Resume-Expert</code></pre>
    </li>
    <li><strong>Create a virtual environment and activate it:</strong>
        <pre><code>python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`</code></pre>
    </li>
    <li><strong>Install the required dependencies:</strong>
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li><strong>Set up your environment variables:</strong>
        <ul>
            <li>Create a <code>.env</code> file in the root directory of the project.</li>
            <li>Add your Google Generative AI API key to the <code>.env</code> file:
                <pre><code>API_KEY=your_google_api_key</code></pre>
            </li>
        </ul>
    </li>
</ol>

<h2 id="usage">Usage</h2>
<p>To run the Streamlit application, use the following command:</p>
<pre><code>streamlit run app.py</code></pre>

<h3>Streamlit App</h3>
<ul>
    <li><strong>Job Description:</strong> Enter the job description in the text area.</li>
    <li><strong>Upload Resume:</strong> Upload the resume in PDF format.</li>
    <li><strong>Actions:</strong>
        <ul>
            <li><strong>Tell Me About the Resume:</strong> Extracts technical skills from the resume.</li>
            <li><strong>Extract Name:</strong> Extracts the candidate's name.</li>
            <li><strong>Extract Location:</strong> Extracts the candidate's location.</li>
            <li><strong>Extract Experience:</strong> Extracts the total experience of the candidate.</li>
        </ul>
    </li>
</ul>

<h2 id="prompts">Prompts</h2>
<ul>
    <li><strong>Technical Skills:</strong>
        <pre><code>You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. Your task is to extract all TECHNICAL SKILLS from the provided resume. List the top 10 to 30 skills mentioned in the resume. Only technical skills remember that and try to give minimum 
        </code></pre>
    </li>
    <li><strong>Name:</strong>
        <pre><code>You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. Extract NAME of the candidate from the resume.
        </code></pre>
    </li>
    <li><strong>Location:</strong>
        <pre><code>You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. Extract Address of the candidate from the resume.
        </code></pre>
    </li>
    <li><strong>Experience:</strong>
        <pre><code>Extract EXPERIENCE of the candidate from the resume total time period candidate worked in numerical value like 3 month 6 month 1 year and so on.
        </code></pre>
    </li>
</ul>

