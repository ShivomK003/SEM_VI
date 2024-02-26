clearvars;

x = [2, 1, 2, -1];
h = [1, 2, 3, 4];

circular_convolution(x, h);


% Function for circular convolution
function y = circular_convolution(x, h)
    % Length of signals
    N = length(x);

    % Initialize figure for circular plotting
    figure;

    % Initialize output signal
    y = zeros(1, N);

    % Iterate through each value of m (n)
    for m = 1:N
        % Step 1: Changing the value of variable m
        n = m;

        % Step 2: Folding of h(m) i.e. h(-m)
        h_flipped = fliplr(h);

        % Step 3: Rotating h(-m) by q
        q = n - 1;
        h_rotated = circshift(h_flipped, [0, q]);

        % Step 4: Multiplication of each x(m) and h(q-m) to get v(m)
        v = x .* h_rotated;

        % Step 5: Summation of all elements in v(m)
        y(m) = sum(v);

        % Plot intermediate steps
        subplot(2, 3, 1);
        polarplot(0, 0);  % Placeholder for polar plot

        subplot(2, 3, 2);
        polarplot(angle(h), abs(h), 'g', 'LineWidth', 1.5);
        title('Impulse Response h(m)');

        subplot(2, 3, 3);
        polarplot(angle(h_flipped), abs(h_flipped), 'b', 'LineWidth', 1.5);
        title('Folding of h(-m)');

        subplot(2, 3, 4);
        polarplot(angle(h_rotated), abs(h_rotated), 'm', 'LineWidth', 1.5);
        title(['Rotated h(q-m) for q = ' num2str(q)]);

        subplot(2, 3, 5);
        polarplot(angle(x), abs(x), 'r', 'LineWidth', 1.5);
        title('Input Signal x(m)');

        subplot(2, 3, 6);
        polarplot(angle(v), abs(v), 'c', 'LineWidth', 1.5);
        title('Intermediate Output v(m)');

        pause(5);  % Pause to visualize each step
    end

    % Plot the final circular convolution result
    figure;
    stem(1:N, y, 'k', 'LineWidth', 1.5);
    title('Final Circular Convolution Output y(n)');
end
