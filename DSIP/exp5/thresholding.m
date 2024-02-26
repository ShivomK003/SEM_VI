clearvars;
b = imread("kodak_pixpro_fz201_01.jpg");
b = rgb2gray(b);
z = b;
[r c] = size(b);
T = input("Enter value of threshold: ")
for i = 1:1:r
    for j = 1:1:c
        if(b(i, j) < T)
            z(i, j) = 0;
        else
            z(i, j) = 255;
        end
    end 
end
figure(1);
imshow(b);
figure(2);
imshow(z);