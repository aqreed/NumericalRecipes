#=
    Unit tests of the factrl function
=#


@testset "test_negative_value" begin
    #=
        Checks values x < 0
    =#
    x = -1
    let err = nothing
        try
            factrl(x)
        catch err
        end
        @test err isa ArgumentError
    end
end


@testset "test_nonInteger_values" begin
    #=
        Checks float, char values
    =#
    x = 1.1
    let err = nothing
        try
            factrl(x)
        catch err
        end
        @test err isa ArgumentError
    end

    x = 'a'
    let err = nothing
        try
            factrl(x)
        catch err
        end
        @test err isa MethodError
    end
end


@testset "test_factrl" begin
    calculated_value = factrl(1)
    expected_value = 1
    @test isapprox(calculated_value, expected_value; atol=1e-8)

    calculated_value = factrl(5)
    expected_value = 120
    @test isapprox(calculated_value, expected_value; atol=1e-8)

    calculated_value = factrl(10)
    expected_value = factorial(10)
    @test isapprox(calculated_value, expected_value; atol=1e-8)

    calculated_value = factrl(15)
    expected_value = factorial(15)
    @test isapprox(calculated_value, expected_value; atol=1e-8)

    calculated_value = factrl(20)
    expected_value = factorial(20)
    @test isapprox(calculated_value, expected_value; atol=1e-8)
end
