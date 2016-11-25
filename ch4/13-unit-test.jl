#Julia Unit Testing

using FactCheck
f(x) = x^3
facts("cubes") do
    @fact f(2) --> 8
    @fact f(2) --> 7
end

using Base.Test
f(x) = x^3
@test f(2) == 8
@test f(2) == 7
