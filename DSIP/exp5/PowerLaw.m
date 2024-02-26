clearvars;
b = imread("kodak_pixpro_fz201_01.jpg");
b = rgb2gray(b);
b_nor = double(b) / 256;
c = 2;
gamma = 2.8;
f = c * b_nor.^gamma;
subplot(1, 2, 1), imshow(b_nor);
subplot(1, 2, 2), imshow(f)
