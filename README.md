# PDF Generator

PDF Generator uses form input with Django to dynamically generate pdf documents. In this case it was a basic CV template used. but practically it could be used for for example order forms / job application information forms.

## Installation

**pip install -r requirements.txt**

_Requirements.txt_

```python
asgiref==3.7.2
black==23.12.1
click==8.1.7
colorama==0.4.6
Django==5.0.1
mypy-extensions==1.0.0
packaging==23.2
pathspec==0.12.1
pdfkit==1.0.0
platformdirs==4.1.0
sqlparse==0.4.4
tzdata==2023.4
```

## Usage

### Endpoints / templates

-  '/': Form submission ("pdf/accept.html")
-  '/:id": PDF download ("pdf/resume.html")
-  '/list': List of PDFs to download ("pdf/list.html")


## Project Notes
- This was one of my first Django based projects, so the focus was on form / file functionality over styling in the front end (Bootstrap was used to provide basic styling across the templates)
- The first draft contained more basic information, but future versions would aim to use more complex data structures to produce a more detailed PDF in the case of generating CVs for example.
