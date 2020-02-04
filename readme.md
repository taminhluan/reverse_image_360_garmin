exiftool -TagsFromFile V0051076.JPG toimage.jpg

magick V0051076.JPG -crop 50%x100% +repage split_with_magick_%02d.jpg

convert +append split_with_magick_01.jpg split_with_magick_00.jpg out_magick.jpg


B1. Cài đặt exiftool và imagemagick

B2. COPY file app.py vào thư mục 360 và chạy python3

B3. Kết quả ở trong thư mục 360_RESULT