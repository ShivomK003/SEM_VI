clearvars;
b = imread("kodak_pixpro_fz201_01.jpg");
b = rgb2gray(b);
z = 255 - b;
figure(1);
imshow(b);
title("Original")
figure(2);
imshow(z);
title("Negative")