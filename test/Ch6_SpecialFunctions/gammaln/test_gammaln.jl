#=
    Unit tests of the Log Gamma function

    Expected values extracted from:
        [URL] https://keisan.casio.com/exec/system/1180573442
=#


using Test

include("../../../src/nr/Ch6_SpecialFunctions/gammaln/gammaln.jl")
using .mod_gammaln: gammaln


function test_gammaln()
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


function test_gammaln_recurrence()
    #=
        Gamma log function satisfies the recurrence relation:
            gamma(z+1) = z * gamma(z)

        Accordingly, this test checks that:
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
