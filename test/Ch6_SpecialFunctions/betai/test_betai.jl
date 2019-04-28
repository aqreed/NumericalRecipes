#=
    Unit tests of the betai function

    Expected values extracted from:
        [URL] https://www.encyclopediaofmath.org/index.php/Incomplete_beta-function
=#


using Test

include("../../../src/nr/Ch6_SpecialFunctions/betai/betai.jl")
using .mod_betai: betai


function test_betai_x0()
    #=
        Checks betai output for x = 0
    =#
    a, b, x = 0.5, 0.5, 0

    calculated_value = betai(a, b, x)
    expected_value = 0

    @test isapprox(calculated_value, expected_value; atol=1e-8)
end


function test_betai_x1()
    #=
        Checks betai output for x = 1
    =#
    a, b, x = 0.5, 0.5, 1

    calculated_value = betai(a, b, x)
    expected_value = 1

    @test isapprox(calculated_value, expected_value; atol=1e-8)
end


function test_betai_symmetry()
    #=
        Checks relation Ix(a, b) = 1 - Ix-1(b, a)
    =#
    a, b, x = 1, 10, 0.15

    calculated_value = betai(a, b, x) + betai(b, a, 1 - x)
    expected_value = 1

    @test isapprox(calculated_value, expected_value; atol=1e-8)
end


function test_betai_recurrence()
    #=
        Checks relation Ix(a, b) = xIx(a−1, b) + (1−x)Ix(a, b−1)
    =#
    a, b, x = 1, 10, 0.15

    calculated_value = betai(a, b, x) - x * betai(a - 1, b, x) - 
                       (1 - x) * betai(a, b - 1, x)

    expected_value = 0

    @test isapprox(calculated_value, expected_value; atol=1e-8)
end
