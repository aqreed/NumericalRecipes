#=
    Unit tests of the ttest function

    Expected values obtained from HypothesisTests package
=#
using HypothesisTests


@testset "test_ttest_means_0" begin
    #=
        Checks against HypothesisTests
    =#
    data1 = [1, 22, 3, 4, 5, 16, 7, 8, 9]
    data2 = [1.1, 2, 3, 4, 5, 6, 7, 18, 9]

    # Student's "t"
    calculated_value = ttest(data1, data2)[1]
    expected_value = EqualVarianceTTest(data1, data2).t

    @test isapprox(calculated_value, expected_value; atol=1e-6)

    # Student's "significance"
    calculated_value = ttest(data1, data2)[2]
    expected_value = pvalue(EqualVarianceTTest(data1, data2))

    @test isapprox(calculated_value, expected_value; atol=1e-6)
end


@testset "test_ttest_means_1" begin
    #=
        Checks against HypothesisTests
    =#
    data1 = [1, 22, 3, 4, 5, 16]
    data2 = [1.1, 2, 3, 4, 5, 6, 7, 18, 9]
    # Student's "t"
    calculated_value = ttest(data1, data2)[1]
    expected_value = EqualVarianceTTest(data1, data2).t

    @test isapprox(calculated_value, expected_value; atol=1e-6)

    # Student's "significance"
    calculated_value = ttest(data1, data2)[2]
    expected_value = pvalue(EqualVarianceTTest(data1, data2))

    @test isapprox(calculated_value, expected_value; atol=1e-6)
end
