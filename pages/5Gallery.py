from pathlib import Path
import streamlit as st

st.subheader("Gallery")
# Load up to 17 gallery images from a Gallery folder one level up, or from this page's folder.
page_folder = Path(__file__).parent

gallery_folder = page_folder.parent / "Gallery"
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