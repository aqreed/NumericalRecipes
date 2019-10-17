#=
    Unit tests of the avevar function

    Expected values obtained from:
        [URL] http://www.alcula.com/calculators/statistics/variance/
=#


@testset "test_avevar_10" begin
    #=
        Checks average values of an input dataset
    =#
    data = [1, 1, 1, 1, 1]
    calculated_value = avevar(data)[1]
    expected_value = 1.0

    @test isapprox(calculated_value, expected_value; atol=1e-8)
end


@testset "test_avevar_11" begin
    #=
        Checks average values of an input dataset
    =#
    data = [-2, -1, 0, 1, 2]
    calculated_value = avevar(data)[1]
    expected_value = 0.0

    @test isapprox(calculated_value, expected_value; atol=1e-8)
end


@testset "test_avevar_12" begin
    #=
        Checks average values of an input dataset
    =#
    data = [1, 2, 3, 4, 5]
    calculated_value = avevar(data)[1]
    expected_value = 3

    @test isapprox(calculated_value, expected_value; atol=1e-8)
end


@testset "test_avevar_20" begin
    #=
        Checks variance (sample) values of an input dataset
    =#
    data = [1, 1, 1, 1, 1]
    calculated_value = avevar(data)[2]
    expected_value = 0.0

    @test isapprox(calculated_value, expected_value; atol=1e-8)
end


@testset "test_avevar_21" begin
    #=
        Checks variance (sample) values of an input dataset
    =#
    data = [1, 2, 3, 4, 5]
    calculated_value = avevar(data)[2]
    expected_value = 2.5

    @test isapprox(calculated_value, expected_value; atol=1e-8)
end


@testset "test_avevar_22" begin
    #=
        Checks variance (sample) values of an input dataset
    =#
    data = [1, 3, 5, 7, 9]
    calculated_value = avevar(data)[2]
    expected_value = 10.0

    @test isapprox(calculated_value, expected_value; atol=1e-8)
end
