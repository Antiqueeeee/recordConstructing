import gradio

secretKey = "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"


def medicalRecordGenerating(recordTemplate,speech):
    prompt = f'''请你扮演一位医生，根据和患者之间的对话为患者整理一份结构化病历，病历中所有包含的内容及要求会以json的形式给你。对话中未明确提及的内容，只能填入空字符串。注意不要将就诊日期和患者以往的就诊的日期混淆。json中包含键值对，键为病历中的内容，值为该内容的要求。json如下：{recordTemplate},与患者之间的对话如下：{speech}
        '''
    return prompt


with gradio.Column():
    medicalRecord = gradio.TextArea(label="Json病历模板")
    speech = gradio.TextArea(label="医患对话记录")
    inputs = [medicalRecord,speech]
# with gradio.Row():
outputs = gradio.TextArea(label="电子病历")

'{"年份": "该项需要填入就诊年份", "月份": "该项需要填入就诊月份", "面貌改变": "该项需要从[面貌改变、手足增大、多汗、巨人症、头疼、性功能下降]中选择若干项作为内容", "生长激素": "该项需要从[曾使用、未使用]中选择一项作为内容", "视力减退、视野缺损": "该项需要从[有、无]中选择一项作为内容", "眼睑下垂": "该项需要从[有、无]中选择一项作为内容", "向心性肥胖紫纹": "该项需要从[有、无]中选择一项作为内容", "性功能减退": "该项需要从[有、无]中选择一项作为内容", "心悸胸闷": "该项需要从[有、无]中选择一项作为内容", "生长抑素治疗": "该项需要从[曾使用、未使用]中选择一项作为内容", "放射治疗": "该项需要从[曾进行、未进行]中选择一项作为内容", "手术治疗": "该项需要从[曾进行、未进行]中选择一项作为内容", "患者精神": "该项需要从[好、不好]中选择一项作为内容", "胃纳": "该项需要从[可、不可]中选择一项作为内容", "睡眠": "该项需要从[好、不好]中选择一项作为内容", "大小便": "该项需要从[正常、不正常]中选择一项作为内容", "体重下降": "该项需要从[无体重明显下降、有体重明显下降]中选择一项作为内容", "新型冠状病毒肺炎风险评估流行病学史": "该项需要从[阴性、阳性]中选择一项作为内容"}'
demo = gradio.Interface(
    fn = medicalRecordGenerating
    ,inputs=inputs
    ,outputs=outputs
)
app, local_url, share_url = demo.launch()



