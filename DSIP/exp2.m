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


% --PERFORMING OPERATIONS ON THE ABOVE SIGNALS-- %

figure(2);

% Adding Unit Step Signal and Increasing Exponential Signal
subplot(2,4,1);
added_signal = zeros(size(sx));
for i = 1:length(sx)
    added_signal(i) = sy(i) + cy(i);
end
stem(sx, added_signal);
title('Added');
% Subtracting Ramp Signal and Unit Step Signal
subplot(2,4,2);
subtracted_signal = zeros(size(sx));
for i = 1:length(sx)
    subtracted_signal(i) = sy(i) - cy(i);
end
stem(sx, subtracted_signal);
title('Subtracted');

% Multiplying Ramp Signal and Cosine Signal
subplot(2,4,3);
multiplied_signal = zeros(size(sx));
for i = 1:length(sx)
    multiplied_signal(i) = sy(i) * cy(i);
end
stem(sx, multiplied_signal);
title('Multiplied');

% Upscale and Downscale the Added Signal by 2
subplot(2,4,4);
upscaled_added_signal = added_signal * 2;
stem(sx, upscaled_added_signal);
title('Upscaled');

subplot(2,4,5);
downscaled_added_signal = added_signal / 2;
stem(sx, downscaled_added_signal);
title('Downscaled');

% Shift Operation on Multiplied Signal
shift_amount = 5;

subplot(2,4,6);
shifted_multiplied_signal_advance = zeros(size(sx));
for i = 1:length(sx)-shift_amount
    shifted_multiplied_signal_advance(i+shift_amount) = multiplied_signal(i);
end
stem(sx, shifted_multiplied_signal_advance);
title('R Shifted');


subplot(2,4,7);
shifted_multiplied_signal_delay = zeros(size(sx));
for i = shift_amount+1:length(sx)
    shifted_multiplied_signal_delay(i-shift_amount) = multiplied_signal(i);
end
stem(sx, shifted_multiplied_signal_delay);
title('L Shifted');
