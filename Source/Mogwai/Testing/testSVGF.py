def render_graph_DefaultRenderGraph():
	g = RenderGraph("DefaultRenderGraph")
	loadRenderPassLibrary("AccumulatePass.dll")
	loadRenderPassLibrary("MinimalPathTracer.dll")
	loadRenderPassLibrary("ErrorMeasurePass.dll")
	loadRenderPassLibrary("PixelInspectorPass.dll")
	loadRenderPassLibrary("DebugPasses.dll")
	loadRenderPassLibrary("GBuffer.dll")
	loadRenderPassLibrary("SamplePassLibrary.dll")
	loadRenderPassLibrary("PassLibraryTemplate.dll")
	loadRenderPassLibrary("PathTracer.dll")
	loadRenderPassLibrary("SVGFPass.dll")
	loadRenderPassLibrary("TemporalDelayPass.dll")
	SVGFPass = RenderPass("SVGFPass", {'Enabled': True, 'Iterations': 4, 'FeedbackTap': 1, 'VarianceEpsilon': 9.999999747378752e-05, 'PhiColor': 10.0, 'PhiNormal': 128.0, 'Alpha': 0.05000000074505806, 'MomentsAlpha': 0.20000000298023224})
	g.addPass(SVGFPass, "SVGFPass")
	GBufferRaster = RenderPass("GBufferRaster", {'cull': CullMode.CullBack})
	g.addPass(GBufferRaster, "GBufferRaster")
	#PathTracer = RenderPass("PathTracer", {'mSharedParams': PathTracerParams(thresholdDirect=10.000000, samplesPerPixel=1, useAnalyticLights=1, thresholdIndirect=10.000000, maxBounces=3, forceAlphaOne=1, clampDirect=0, useEmissiveLights=1, clampIndirect=0, useEnvLight=1, useBRDFSampling=1, useEnvBackground=1, useMIS=1, misHeuristic=1, misPowerExponent=2.000000, useEmissiveLightSampling=1, probabilityAbsorption=0.200000, useRussianRoulette=0, useFixedSeed=0), 'mSelectedSampleGenerator': 0, 'mSelectedEmissiveSampler': EmissiveLightSamplerType.LightBVH})
	PathTracer = RenderPass("MegakernelPathTracer", {'mSharedParams': PathTracerParams(thresholdDirect=10.000000, samplesPerPixel=1, useAnalyticLights=1, thresholdIndirect=10.000000, maxBounces=3, forceAlphaOne=1, clampDirect=0, useEmissiveLights=1, clampIndirect=0, useEnvLight=1, useBRDFSampling=1, useEnvBackground=1, useMIS=1, misHeuristic=1, misPowerExponent=2.000000, useEmissiveLightSampling=1, probabilityAbsorption=0.200000, useRussianRoulette=0, useFixedSeed=0), 'mSelectedSampleGenerator': 0, 'mSelectedEmissiveSampler': EmissiveLightSamplerType.Uniform})
	g.addPass(PathTracer, "PathTracer")
	g.addEdge("PathTracer.color", "SVGFPass.Color")
	g.addEdge("GBufferRaster.posW", "PathTracer.posW")
	g.addEdge("PathTracer.albedo", "SVGFPass.Albedo")
	g.addEdge("GBufferRaster.normW", "PathTracer.normalW")
	g.addEdge("GBufferRaster.bitangentW", "PathTracer.bitangentW")
	g.addEdge("GBufferRaster.faceNormalW", "PathTracer.faceNormalW")
	g.addEdge("GBufferRaster.diffuseOpacity", "PathTracer.mtlDiffOpacity")
	g.addEdge("GBufferRaster.specRough", "PathTracer.mtlSpecRough")
	g.addEdge("GBufferRaster.emissive", "PathTracer.mtlEmissive")
	g.addEdge("GBufferRaster.matlExtra", "PathTracer.mtlParams")
	g.addEdge("GBufferRaster.emissive", "SVGFPass.Emission")
	g.addEdge("GBufferRaster.posW", "SVGFPass.WorldPosition")
	g.addEdge("GBufferRaster.normW", "SVGFPass.WorldNormal")
	g.addEdge("GBufferRaster.pnFwidth", "SVGFPass.PositionNormalFwidth")
	g.addEdge("GBufferRaster.linearZ", "SVGFPass.LinearZ")
	g.addEdge("GBufferRaster.mvec", "SVGFPass.MotionVec")
	g.markOutput("SVGFPass.Filtered image")
	g.markOutput("GBufferRaster.mvec")
	g.markOutput("PathTracer.color")
	g.markOutput("GBufferRaster.posW")
	g.markOutput("PathTracer.albedo")
	g.markOutput("GBufferRaster.normW")
	g.markOutput("GBufferRaster.bitangentW")
	g.markOutput("GBufferRaster.diffuseOpacity")
	g.markOutput("GBufferRaster.specRough")
	g.markOutput("GBufferRaster.emissive")
	g.markOutput("GBufferRaster.matlExtra")
	g.markOutput("GBufferRaster.emissive")
	g.markOutput("GBufferRaster.posW")
	g.markOutput("GBufferRaster.normW")
	g.markOutput("GBufferRaster.pnFwidth")
	g.markOutput("GBufferRaster.linearZ")
	return g

DefaultRenderGraph = render_graph_DefaultRenderGraph()
try: m.addGraph(DefaultRenderGraph)
except NameError: None