% unit step signal
subplot(2,4,1);
ux = -10:1:10;
uy = zeros(size(ux));
uy(ux>=0) = 1;
unit_step_signal = stem(ux,uy);

% ramp signal
subplot(2,4,2);
rx = linspace(-10, 11, 21);
count = 1;
ry = zeros(size(rx));
for x = rx
    if x >= 0
        ry(count) = x;
    end
    count = count + 1;
end
clear count;
clear x;
ramp_signal = stem(rx, ry);


% exponential signal
subplot(2, 4, 3);
ex = 1:1:20;
iey = zeros(size(ex));
dey = zeros(size(ex));
for x = ex
    iey(x) = 2^x;
    dey(x) = 0.5^x;
end
clear x; 
inc_exp_signal = stem(ex, iey);

subplot(2, 4, 4);
ex = 1:1:20;
dey = zeros(size(ex));
for x = ex
    dey(x) = 0.5^x;
end
clear x; 
dec_exp_signal = stem(ex, dey);

% impulse signal
subplot(2, 4, 5);
ix = -10:1:10;
iy = zeros(size(ix));
iy(ix==0) = 10;
imp_signal = stem(ix,iy);

% sine signal
subplot(2, 4, 6);
sx = linspace(-2*pi, 2*pi, 40);
sy = sin(sx);
sin_signal = stem(sx, sy);

% cosine signal
subplot(2, 4, 7);
cx = linspace(-2*pi, 2*pi, 40);
cy = cos(cx);
cosine_signal = stem(cx, cy);