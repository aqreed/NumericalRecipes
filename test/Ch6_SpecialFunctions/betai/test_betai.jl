#=
    Unit tests of the betai function

    Expected values obtained from:
        [URL] https://www.encyclopediaofmath.org/index.php/Incomplete_beta-function
=#


@testset "test_betai_x0" begin
    #=
        Checks betai output for x = 0
    =#
    a, b, x = 0.5, 0.5, 0

    calculated_value = betai(a, b, x)
    expected_value = 0

    @test isapprox(calculated_value, expected_value; atol=1e-8)
end


@testset "test_betai_x1" begin
    #=
        Checks betai output for x = 1
    =#
    a, b, x = 0.5, 0.5, 1

    calculated_value = betai(a, b, x)
    expected_value = 1

    @test isapprox(calculated_value, expected_value; atol=1e-8)
end


@testset "test_betai_symmetry" begin
    #=
        Checks relation Ix(a, b) = 1 - Ix-1(b, a)
    =#
    a, b, x = 1, 10, 0.15

    calculated_value = betai(a, b, x) + betai(b, a, 1 - x)
    expected_value = 1

    @test isapprox(calculated_value, expected_value; atol=1e-8)
end


@testset "test_betai_recurrence" begin
    #=
        Checks relation Ix(a, b) = xIx(a−1, b) + (1−x)Ix(a, b−1)
    =#
    a, b, x = 1, 10, 0.15

    calculated_value = betai(a, b, x) - x * betai(a - 1, b, x) - 
                       (1 - x) * betai(a, b - 1, x)

    expected_value = 0

    @test isapprox(calculated_value, expected_value; atol=1e-8)
end
