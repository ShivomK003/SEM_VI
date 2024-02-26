clearvars;


x = [1, 2, 0.5, 1];
h = [1, 2, 1, -1];

linear_convolution(x, h);
% Function for linear convolution without conv function
function y = linear_convolution(x, h)
    % Lengths of input signals
    M = length(x);
    N = length(h);

    % Length of output signal
    L = M + N - 1;

    % Zero-pad signals
    x_padded = [zeros(1, N-1), x];
    h_padded = [flip(h), zeros(1, M - 1)];

    % Initialize output signal
    y = zeros(1, L);

    % Initialize figure for plotting
    figure;

    % Iterate through each value of m
    for m = 1:L
        % Step 2: Shifting h(-m) by q
        q = m - 1;
        h_shifted = zeros(1, L);
        start_index = max(1, 1 + q);
        end_index = min(L, N + q);
        h_shifted(start_index:end_index) = h_padded(1:end_index-start_index+1);

        % Step 3: Multiply x(m) and h(q-m)
        v = x_padded .* h_shifted;

        % Step 4: Sum of all values of v(m) to obtain y(n)
        y(m) = sum(v);

        % Plot intermediate steps
        subplot(4, 1, 1);
        stem(1:M, x, 'r', 'LineWidth', 1.5);
        title('Input Signal x(m)');

        subplot(4, 1, 2);
        stem((-1):(N-2), h, 'g', 'LineWidth', 1.5);
        title('Impulse Response h(m)');

        subplot(4, 1, 3);
        stem(1:L, h_shifted, 'b', 'LineWidth', 1.5);
        title(['Shifted h(q-m) for q = ' num2str(q)]);

        subplot(4, 1, 4);
        stem((-2):(L-3), v, 'm', 'LineWidth', 1.5);
        title('Intermediate Output v(m)');

        pause(5);  % Pause to visualize each step
    end

    % Plot the final convolution result
    figure;
    stem(-1:L-2, y, 'k', 'LineWidth', 1.5);
    title('Final Convolution Output y(n)');
end
