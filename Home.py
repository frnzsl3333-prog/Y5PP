# --- Import required libraries ---
from pathlib import Path
import streamlit as st

# --- HOME PAGE ---
st.title("Welcome to My Year 5 Passion Project!")

# Short introduction
st.write("""
Hello! My name is **Deepak Perina** and this is my **Fried Night Footy App**.  

This app is my **Year 5 passion project**, where I learned how to:
- Code in **Python**
- Use **Streamlit** to make interactive web apps
""")

# Personal journey section
st.subheader("My Learning Journey")
st.write("""
When I started this project, I had never made a game or chart before.  
I learned step by step:
1. How to **take input** from the user using Streamlit.
2. How to **simulate NRL matches** with random tries.
3. How to **display scores and match results** in a fun way.
4. How to create **graphs** like tried and conversions.
5. How to **experiment with colors** and make the app look lively.
""")

# Motivation / reflection
st.subheader("Why I Chose This Project")
st.write("""
I love NRL and wanted to combine it with coding.  
This project taught me that **coding can be fun and creative**.  
I can see how math, logic, and technology work together to make games and simulations.
""")

# Thank you note
st.subheader("Thank You")
st.write("""A big thank you to Mrs Baxter, Mr Elliot and Middle School Office team for giving us the opporunity to present our passion. Special thanks to my parents for supporting this at home.""")

st.subheader("Gallery")
# Load up to 17 gallery images from a Gallery folder, or from this page's folder.
page_folder = Path(__file__).parent
gallery_folder = page_folder / "Gallery"
image_folder = gallery_folder if gallery_folder.is_dir() else page_folder
image_extensions = {".png", ".jpg", ".jpeg", ".gif", ".webp"}
gallery_images = sorted(
	(path for path in image_folder.iterdir()
	 if path.is_file() and path.suffix.lower() in image_extensions
	 and path.name.lower() not in {"myjourney.png", "mycodejourney.png"}),
	key=lambda path: path.name.lower(),
)[:17]

if gallery_images:
	columns = st.columns(3)
	for index, image_path in enumerate(gallery_images):
		with columns[index % 3]:
			st.image(str(image_path), caption=f"📸 {image_path.stem}", use_container_width=True)
else:
	st.info("No gallery images found. Add up to 17 image files to the Gallery folder.")