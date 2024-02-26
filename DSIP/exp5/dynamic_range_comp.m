clearvars;
b = imread("kodak_pixpro_fz201_01.jpg");
b = rgb2gray(b);
b_nor = double(b) / 256;
c = 0.5;
f = c * log(1 + (b_nor));
subplot(1, 2, 1), imshow(b_nor);
subplot(1, 2, 2), imshow(f)
