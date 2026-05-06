# Voice Pro：把语音识别、翻译、TTS 和配音整合到一个本地 WebUI

Voice Pro 是一个面向创作者和开发者的 AI 语音工作台。它用 Gradio 做 WebUI，把视频下载、音频抽取、人声分离、语音识别、字幕生成、翻译、TTS、零样本声音克隆、多语言配音整合在一个流程里。

它不是一个 coding agent，也不是代码开发框架。它更适合放在 AI 时代开发效率工具库里的“多模态内容生产与语音流水线”位置：当开发者需要做教程视频、产品演示、课程字幕、播客配音、语音数据预处理、跨语言内容分发时，它能把原本分散在多个工具里的步骤合并起来。

## 它解决什么问题

围绕音视频内容的开发和发布，经常会遇到这些重复工作：

- 从 YouTube 或本地视频里提取音频。
- 把人声和背景音乐分离。
- 用 Whisper 系列模型做语音识别和字幕。
- 把字幕翻译成多种语言。
- 用 TTS 生成目标语言语音。
- 用声音克隆让配音保持接近原始说话人的音色。
- 把字幕、翻译和配音串成一个可复用流程。

Voice Pro 的价值是把这些环节包成一个 WebUI，而不是要求用户自己拼 `yt-dlp`、Demucs、Whisper、翻译库和 TTS 项目。

## 核心能力

### Dubbing Studio

Voice Pro 的 Dubbing Studio 是一个一体化配音工作台。它支持 YouTube 下载、音频提取、人声分离、字幕识别、翻译和 TTS 输出。官方 README 里还说明它支持 ffmpeg 兼容格式，输出可以是 WAV、FLAC、MP3。

这对开发者的实际价值在于：如果你要给一个产品 demo、技术教程或研究视频做多语言版本，不需要把每一步拆到不同工具里跑。

### Speech-to-Text

项目集成了多种 Whisper 相关方案：

- Whisper
- Faster-Whisper
- Whisper-Timestamped
- WhisperX

这些能力适合生成字幕、转录会议/访谈/课程，也适合把语音资料转成后续可以进入 RAG、总结或翻译流程的文本。

### Translation

Voice Pro 支持 100+ 语言的翻译流程，README 中提到使用 Deep-Translator，付费版本另有 Azure Translator。对开源版本来说，它的重点是把字幕文件和语音识别结果接入翻译流程。

### Text-to-Speech 和声音克隆

Voice Pro 集成了多种 TTS / voice cloning 方案：

- Edge-TTS
- kokoro
- F5-TTS
- E2-TTS
- CosyVoice

其中 F5-TTS、E2-TTS、CosyVoice 面向 zero-shot voice cloning；Edge-TTS 则覆盖大量语言和声音。它适合做多语言讲解、播客草稿、教程配音和语音产品原型。

### Real-Time Translation

项目还提供实时识别和翻译入口，可配置音频输入。这更接近“语音助手 / 会议翻译 / 实时字幕”原型工具，而不是传统音频编辑器。

## 为什么它属于这个 awesome 项目

AI 时代的开发效率不只发生在代码编辑器里。越来越多开发工作会涉及多模态材料：

- 把产品演示录屏做成多语言版本。
- 把技术会议或访谈转成结构化文本。
- 给教程视频生成字幕和配音。
- 为语音应用准备样本、字幕、翻译和测试数据。
- 快速验证 TTS、voice cloning、语音识别链路。

Voice Pro 的价值是把这些语音相关能力放进一个可本地运行的 WebUI。它不是“开发框架”，但它能显著减少 AI 内容生产、语音产品原型和多语言发布中的工具切换成本。

## 使用边界和注意事项

这个项目也有明显边界：

- 官方 README 说明，由于团队转向 WeConnect 开发，Voice Pro 暂时无法持续更新。
- README 同时说明代码已全部开源并免费，可自由分发和修改。
- 项目页面标注 License 为 GPL-3.0。
- 官方提示 Windows + NVIDIA GPU 运行效果较好；Mac 和 Linux 虽列在系统要求中，但 README 里也提到相关运行情况没有充分验证。
- 初次安装会下载较大的模型和依赖，可能需要较长时间。
- 声音克隆、名人参考音色和配音能力涉及授权、肖像/声音权和平台规则，实际使用时必须谨慎。

因此它适合被记录为“可用但需要注意维护状态和运行环境”的工具，而不是无条件推荐给所有开发者。

## 适合谁使用

- 做 AI 教程、产品 demo、课程或播客的开发者。
- 需要批量处理字幕、翻译和配音的创作者。
- 正在构建语音应用、字幕应用或 dubbing workflow 的团队。
- 需要测试 Whisper、TTS、voice cloning 组合链路的工程师。
- 想把语音资料转成文本再进入总结、检索或知识库流程的人。

## 项目信息

- GitHub: https://github.com/abus-aikorea/voice-pro
- 技术栈: Python, Gradio, Whisper, Demucs, Edge-TTS, F5-TTS, E2-TTS, CosyVoice, kokoro, yt-dlp
- License: GPL-3.0
- 当前 GitHub 页面显示约 8.8k stars，主仓库公开。
- 系统要求: Windows 10/11、Linux、Mac；推荐 NVIDIA CUDA 12.4、4GB+ VRAM、20GB+ 磁盘空间。

## 推荐 awesome 条目

```markdown
- [Voice Pro](https://github.com/abus-aikorea/voice-pro) - Gradio WebUI for speech recognition, translation, subtitle generation, TTS, voice cloning, and multilingual dubbing workflows. `Python` `GPL-3.0`
```
