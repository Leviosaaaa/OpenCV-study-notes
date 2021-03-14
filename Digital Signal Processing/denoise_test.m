%% Denoise example
    clear;
    close all;
    clc;
    addpath('FISTA');
%% Data input
    img_clr = imread('../img_ori.jpg');
%     img_gray = double(rgb2gray(img_clr));
%     X = img_gray ./ 255;
%     b = X + 3e-1 * rand(size(X));
%     b = imgaussfilt(b, 1.5, 'FilterSize', 9);
    img_noise = imread('../img_noise.jpg');
    b = double(rgb2gray(img_noise)) ./ 255;
%% Parameter
    lambda = 0.1;
    max_iter = 200;
    % [X_opt, h] = denoise_algo(b, lambda, max_iter, -Inf, Inf);
    [FX_opt, g] = Fdenoise_algo(b, lambda, max_iter, -Inf, Inf);
%% Plot
    b_scale = uint8(255 * b);
    % x_scale = uint8(X_opt * 255);
    Fx_scale = uint8(FX_opt * 255);
    subplot(1, 2, 1);
    imshow(b_scale);
    title('Corrupted image');
    subplot(1, 2, 2);
    imshow(x_scale);
    title('FISTA image');
%     subplot(1, 2, 2);
%     imshow(Fx_scale);
%     title('MFISTA image');
    imwrite(b_scale, 'Corrupted_image.jpg')
%     imwrite(x_scale, 'FISTA_image.jpg')
    imwrite(Fx_scale, '200MFISTA_image.jpg')