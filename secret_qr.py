import qrcode


data = "I'm Akhiliny an undergraduate Software Engineering student at Sabaragamuwa University of Sri Lanka, strongly focused on Data Engineering, Data Science, and Data Analytics. I have experience with Big Data technologies like Hadoop, Spark, SQL, and Python, along with hands-on knowledge of ETL pipelines, data warehousing, and data visualization. Skilled in leveraging cloud platforms, I focus on enhancing data processing and building scalable data solutions. Passionate about data-driven environments, I enjoy collaborating with teams to develop innovative solutions that drive meaningful insights."


qr = qrcode.QRCode(
    version=1,  
    error_correction=qrcode.constants.ERROR_CORRECT_L,  
    box_size=10,  
    border=4  
)


qr.add_data(data)
qr.make(fit=True)


img = qr.make_image(fill="black", back_color="white")
img.save("secret_qrcode.png")

print("Secret QR Code generated successfully!")
