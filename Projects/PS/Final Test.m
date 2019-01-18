% 4. Nickel powders are used in coatings used to shield electronic equipment. 
% A random sample is selected, and the sizes of nickel particles in each coating 
% are recorded ( they are assumed to be approximately normally distributed)

X = [3.26 1.89 2.42 2.03 3.07 2.95 1.39 3.06 2.46 3.35 1.56 1.79 1.76 3.82 2.42 2.96];

% b) At the 1% significance level, on average, do these nickel particles seem to be smaller than 3?

sigma = std(X);

H0 = 3; 

H1 = mean(X); % lower than H0 -> we do a left test

% alternate hypothesis H1
% average size of nickel particles < 3

len_X = length(X);
test_st = (H1 - H0) / (sigma / sqrt(len_X)); % test statistic
fprintf("Test statistic: tt=%4.4f\n", test_st);

% significance level
alpha = 0.01;
rreg = tinv(alpha, len_X - 1);
fprintf("Rejection region: (%4.4f, inf)\n", rreg);

% p - value
p_value = tcdf(test_st, len_X - 1);
fprintf("Significance level: %.2f, P-Value: p=%4.4f\n", alpha, p_value);

% conclusion
if (p_value < alpha)
  fprintf("Reject H0, accept H1. average size of nickel particles is lower than 3\n");
else
  fprintf("Accept H0, reject H1. average size of nickel particles is NOT lower than 3\n");
end