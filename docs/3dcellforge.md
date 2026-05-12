# 3DCellForge：浏览器里的 3D 细胞生成与探索工作台

3DCellForge 是一个 React + Three.js 原型，用来在浏览器里生成、加载和探索 3D 生物细胞模型。它把细胞模型展示、细胞器信息面板、显微镜参考图、截图、GLB 导出和 image-to-3D 生成后端放进同一个 WebGL 工作台。

它适合放进这个 awesome 项目的 “3D And Asset Generation” 分类。原因不是它只做了一个漂亮的 3D demo，而是它展示了一个可被开发者复用的 AI 资产生成工作流：参考图上传、云端或本地生成 GLB、缓存模型、在浏览器里检查材质和交互表现，再导出或继续用于演示。

## 它解决什么问题

做 3D 原型时，开发者经常卡在资产环节。即使前端已经能写 Three.js 或 React Three Fiber，仍然需要模型、材质、灯光、交互面板和导入导出流程。生物细胞这类主题还多了一层复杂度：模型既要可视化，又要能承载细胞器说明、参考图和对比视图。

3DCellForge 把这个流程压缩成一个浏览器工作台：

1. 用 React Three Fiber 展示可旋转、缩放的 3D 细胞场景；
2. 在侧边面板查看细胞器细节、显微镜参考和生物学笔记；
3. 通过 Tripo 云端或 Hunyuan3D 本地服务从图片生成 3D 模型；
4. 导入已有 `.glb` 或自包含 `.gltf`；
5. 缓存生成后的 GLB，方便后续截图、演示和复用。

对 AI-native 开发来说，它的价值在于把“生成 3D 资产”和“验证 3D 资产是否能在真实 WebGL 应用中工作”连在了一起。

## 核心能力

### 浏览器内 3D 细胞查看器

项目使用 React、Vite、Three.js、React Three Fiber 和 Drei 搭建交互式细胞查看器。用户可以拖拽旋转、滚轮缩放，并切换 3D proof 模式来检查模型表现。

这让它不只是模型生成脚本，而是一个可直接运行的前端原型。开发者可以拿它作为 WebGL 生物可视化、医学教育 demo、3D 科普页面或 AI 资产工具的起点。

### Image-to-3D 后端

3DCellForge 支持通过本地 Node 后端接入 Tripo 云端 image-to-3D，也支持 Hunyuan3D 本地服务作为备用路径。上传面板还包含 `Auto` 模式，可以按 Tripo、Hunyuan、JS Depth 的顺序降级。

这个设计对开发工作流很实用：API key 留在服务端 `.env.local`，生成后的 GLB 缓存在本地目录，前端不需要直接暴露密钥或依赖临时远程模型 URL。

### GLB 导入、导出和缓存

项目支持导入本地 `.glb` 或自包含 `.gltf`，也支持导出 GLB 和截图。仓库还内置了缓存 demo 模型，方便在不消耗 API credits 的情况下做演示。

这让它更接近“可复用的 3D 资产工作台”，而不是一次性的视觉效果页面。

## 为什么适合 AI 开发效率工具库

这个 awesome 项目关注的是 AI 时代提高开发效率的开源软件。3DCellForge 的位置在于：它展示了 AI 生成 3D 资产如何进入一个真实的前端工程闭环。

典型使用场景包括：

- 快速做 WebGL / React Three Fiber 3D 原型；
- 把 image-to-3D 生成接入浏览器产品；
- 为教育、科研展示或产品 demo 生成可交互模型；
- 验证 Tripo、Hunyuan3D、本地 GLB 导入等多条资产路径；
- 给 AI agent 或开发者提供一个可运行的 3D 资产验证界面。

相比只提供模型生成 API 的项目，3DCellForge 更强调“生成之后怎么用”：模型要能被加载、旋转、截图、导出、缓存，并且能在具体 UI 中承载领域信息。

## 边界和注意点

3DCellForge 目前更像一个高完成度原型和示范工作台，不是通用 3D 引擎，也不是完整的生物医学建模平台。

使用时需要注意：

- Tripo 生成需要 API key 和云端服务；
- Hunyuan3D 本地模式需要另外启动本地 API 服务；
- JS Depth 是降级路径，效果不能替代真实 mesh 生成；
- 生物学内容和模型形态如果用于教学或科研，需要另行校验准确性；
- 生成或上传参考图时仍然要注意版权、隐私和授权。

## 适合谁

- 想快速搭建 3D 交互 demo 的前端开发者；
- 正在做 Three.js / React Three Fiber 原型的团队；
- 想把 image-to-3D 接入产品流程的开发者；
- 需要浏览器内 GLB 导入、检查、截图和导出的工具开发者；
- 研究 AI 资产生成到实际 WebGL 应用闭环的人。

## 项目信息

- GitHub: https://github.com/huangserva/3DCellForge
- 技术栈: React, Vite, Three.js, React Three Fiber, Drei, Framer Motion
- 可选后端: Tripo API, Hunyuan3D local API
- 主要语言: JavaScript
- License: MIT

## Awesome 列表条目

```markdown
- [3DCellForge](https://github.com/huangserva/3DCellForge) - Browser-based 3D cell generation and exploration studio with React Three Fiber, GLB import/export, and optional Tripo or Hunyuan3D image-to-3D backends. `JavaScript` `MIT`
```
