import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

st.set_page_config(
    page_title="QR Code Generator",
    page_icon="🔗",
    layout="centered"
)

st.title("🔗 QR Code Generator")
st.caption("Generate a high-quality QR code from any link")

st.divider()

url = st.text_input(
    "Enter URL",
    placeholder="https://docs.google.com/..."
)

def generate_qr_image(link: str) -> Image.Image:
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color="black",
        back_color="white"
    ).convert("RGB")

    img = img.resize((325, 325), Image.LANCZOS)
    return img


if st.button("Generate QR Code", use_container_width=True):
    if not url.strip():
        st.error("Please enter a valid URL")
    else:
        qr_image = generate_qr_image(url)

        st.success("QR Code generated successfully")

        st.image(
            qr_image,
            caption="Preview (325 × 325)",
            width=325
        )

        buffer = BytesIO()
        qr_image.save(buffer, format="PNG")
        buffer.seek(0)

        st.download_button(
            label="⬇ Download QR Code",
            data=buffer,
            file_name="qr_code.png",
            mime="image/png",
            use_container_width=True
        )

st.divider()
st.caption("Built with Streamlit • QR size: 325×325 px")
