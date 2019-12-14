#=
    Unit tests of the Log Gamma function

    Expected values obtained from:
        [URL] https://keisan.casio.com/exec/system/1180573442
=#


@testset "test_gammaln_error" begin
    #=
        Checks gammaln erroneous input
    =#
    x = -0.1

    let err = nothing
        try
            gammaln(x)
        catch err
        end

        @test err isa Exception
    end
end


@testset "test_gammaln" begin
    #=
        Checks values x > 0
    =#
    x1, x2, x3, x4 = 0.01, 1.0, 2.0, 5.0

    c1 = gammaln(x1)
    c2 = gammaln(x2)
    c3 = gammaln(x3)
    c4 = gammaln(x4)

    calculated_value = [c1, c2, c3, c4]
    expected_value = [4.599479878042021722514, 0,
                      0, 3.178053830347945619647]

    @test isapprox(calculated_value, expected_value; atol=1e-8)
end


@testset "test_gammaln_recurrence" begin
    #=
        Gamma function satisfies the recurrence relation:
            gamma(z+1) = z * gamma(z)

        Accordingly, this test checks that gamma log satisfies:
            gammaln(z+1) = ln(z) + gammaln(z)
    =#
    x1, x2, x3, x4 = 0.001, 1.1, 3.32, 23.11

    c1 = gammaln(x1 + 1) - (log(x1) + gammaln(x1))
    c2 = gammaln(x2 + 1) - (log(x2) + gammaln(x2))
    c3 = gammaln(x3 + 1) - (log(x3) + gammaln(x3))
    c4 = gammaln(x4 + 1) - (log(x4) + gammaln(x4))

    calculated_value = [c1, c2, c3, c4]
    expected_value = [0, 0, 0, 0]

    @test isapprox(calculated_value, expected_value; atol=1e-8)
end


@testset "test_gammaln_factorial" begin
    #=
        Gamma function satisfies the recurrence relation for
        positive integer values:
            gamma(z) = (z-1)!

        Accordingly, this test checks that gamma log satisfies:
            exp[gammaln(z)] = (z-1)!
    =#
    x1, x2, x3, x4 = 1, 2, 6, 9

    c1 = exp(gammaln(x1)) - factorial(x1 - 1)
    c2 = exp(gammaln(x2)) - factorial(x2 - 1)
    c3 = exp(gammaln(x3)) - factorial(x3 - 1)
    c4 = exp(gammaln(x4)) - factorial(x4 - 1)

    calculated_value = [c1, c2, c3, c4]
    expected_value = [0, 0, 0, 0]

    @test isapprox(calculated_value, expected_value; atol=1e-4)
end
