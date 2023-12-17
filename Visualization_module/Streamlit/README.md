### Modules
**cv_api.py** - local web server on Flask for model inference for painting classification (artist search)

**streamlit_app.py** - local web application based on streamlit for visualization of modules

### Usage tips:
Put [inceptionV3](https://drive.google.com/file/d/1PX24dwQyEKfwcCWMAT5EFV_a3gRYgAMC/view?usp=sharing) in `cv_module/models` directory.

### Launching modules
1. First, on the command line from this directory:
    
         python cv_api.py


2. After on the command line from this directory:

         streamlit run streamlit_app.py