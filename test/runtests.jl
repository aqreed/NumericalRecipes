using Test
using NumericalRecipes


@testset "test_betacf" begin include("Ch6_SpecialFunctions/betacf/test_betacf.jl") end
@testset "test_betai" begin include("Ch6_SpecialFunctions/betai/test_betai.jl") end
@testset "test_gammaln" begin include("Ch6_SpecialFunctions/gammaln/test_gammaln.jl") end
@testset "test_avevar" begin include("Ch13_StatisticalDescriptionOfData/avevar/test_avevar.jl") end
@testset "test_ttest" begin include("Ch13_StatisticalDescriptionOfData/student_ttest/different_means/test_ttest.jl") end
@testset "test_tutest" begin include("Ch13_StatisticalDescriptionOfData/student_ttest/different_variances/test_tutest.jl") end
