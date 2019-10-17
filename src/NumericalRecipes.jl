module NumericalRecipes

	export betacf, betai, gammaln, avevar, ttest, tutest, tptest

	include("numericalrecipes/Ch6_SpecialFunctions/betacf/betacf.jl")
	include("numericalrecipes/Ch6_SpecialFunctions/betai/betai.jl")
	include("numericalrecipes/Ch6_SpecialFunctions/gammaln/gammaln.jl")
	include("numericalrecipes/Ch13_StatisticalDescriptionOfData/avevar/avevar.jl")
	include("numericalrecipes/Ch13_StatisticalDescriptionOfData/student_ttest/paired_samples/tptest.jl")
	include("numericalrecipes/Ch13_StatisticalDescriptionOfData/student_ttest/different_means/ttest.jl")
	include("numericalrecipes/Ch13_StatisticalDescriptionOfData/student_ttest/different_variances/tutest.jl")

end # module
