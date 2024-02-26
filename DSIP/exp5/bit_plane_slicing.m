clearvars;
b = imread("kodak_pixpro_fz201_01.jpg");
b = rgb2gray(b);
b1 = [];
b2 = [];
b3 = [];
b4 = [];
b5 = [];
b6 = [];
b7 = [];
b8 = [];

for i = 1:256
    for j = 1:256
        t = int2bit(b(i, j), 8, false);
        b1(i, j) = t(1,1);
        b2(i, j) = t(2,1);
        b3(i, j) = t(3,1);
        b4(i, j) = t(4,1);
        b5(i, j) = t(5,1);
        b6(i, j) = t(6,1);
        b7(i, j) = t(7,1);
        b8(i, j) = t(8,1);
    end
end

figure;
subplot(3,3,1);
imshow(b);
subplot(3,3,2);
imshow(b1);
subplot(3,3,3);
imshow(b2);
subplot(3,3,4);
imshow(b3);
subplot(3,3,5);
imshow(b4);
subplot(3,3,6);
imshow(b5);
subplot(3,3,7);
imshow(b6);
subplot(3,3,8);
imshow(b7);
subplot(3,3,9);
imshow(b8);