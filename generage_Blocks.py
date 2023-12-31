import gradio

secretKey = "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"


def medicalRecordGenerating(recordTemplate,speech):
    prompt = f'''请你扮演一位医生，根据和患者之间的对话为患者整理一份结构化病历，病历中所有包含的内容及要求会以json的形式给你。对话中未明确提及的内容，只能填入空字符串。注意不要将就诊日期和患者以往的就诊的日期混淆。json中包含键值对，键为病历中的内容，值为该内容的要求。json如下：{recordTemplate},与患者之间的对话如下：{speech}
        '''
    return prompt



with gradio.Column():
    recordTemplate = gradio.TextArea(label="Json病历模板")
    speech = gradio.TextArea(label="对话记录")
    
    
with gradio.Blocks() as demo:
    with gradio.Column():
        gradio.Examples(
        ['{"年份": "该项需要填入就诊年份", "月份": "该项需要填入就诊月份", "面貌改变": "该项需要从[面貌改变、手足增大、多汗、巨人症、头疼、性功能下降]中选择若干项作为内容", "生长激素": "该项需要从[曾使用、未使用]中选择一项作为内容", "视力减退、视野缺损": "该项需要从[有、无]中选择一项作为内容", "眼睑下垂": "该项需要从[有、无]中选择一项作为内容", "向心性肥胖紫纹": "该项需要从[有、无]中选择一项作为内容", "性功能减退": "该项需要从[有、无]中选择一项作为内容", "心悸胸闷": "该项需要从[有、无]中选择一项作为内容", "生长抑素治疗": "该项需要从[曾使用、未使用]中选择一项作为内容", "放射治疗": "该项需要从[曾进行、未进行]中选择一项作为内容", "手术治疗": "该项需要从[曾进行、未进行]中选择一项作为内容", "患者精神": "该项需要从[好、不好]中选择一项作为内容", "胃纳": "该项需要从[可、不可]中选择一项作为内容", "睡眠": "该项需要从[好、不好]中选择一项作为内容", "大小便": "该项需要从[正常、不正常]中选择一项作为内容", "体重下降": "该项需要从[无体重明显下降、有体重明显下降]中选择一项作为内容", "新型冠状病毒肺炎风险评估流行病学史": "该项需要从[阴性、阳性]中选择一项作为内容"}']
        ,recordTemplate
        ,label="病历模板样例"
    )
    gradio.Examples(
        ['\n患者：医生您好，我月经紊乱3年多了，也不知道原因是什么。\n医生：月经紊乱前是否生活压力很大？或者生活中出现了重大变故？\n患者：没有，都挺正常的。\n医生：例假会持续多长时间？量正常嘛？\n患者：可能要有7、8天左右，量比较少。\n医生：之前有没有去看过医生？\n患者：2023年5月份的时候参加体检发现泌乳素升高，然后就去我们本地的医院看来着，医生让我做一个垂体的磁共振，报告上说怀疑是垂体腺瘤。\n医生：那后来给你开了什么药物？有没有做过放射治疗？\n患者：没有。\n医生：那你自己有没有找什么药吃？\n患者：没有。\n医生：这几年你有没有觉得看东西没有以前清楚了？看到的视野跟原来一样大吗？\n患者：我视力还好，这几年里没什么变化。\n医生：眼睑呢？跟之前比有没有什么变化？\n患者：没有，没什么变化。\n医生：有没有觉得手脚比以前胖了？\n患者：也没有。\n医生：这几年有变胖嘛？身上有那种变胖之后的纹路嘛？\n患者：没有，这几年我体重没什么变化，没变胖。\n医生：那有没有心悸、胸闷之类的感觉？\n患者：没有，没有这些感觉。\n医生：有孩子了嘛？\n患者：有孩子了。\n医生：有溢乳嘛？\n患者：没有。\n医生：以前做过什么手术嘛？\n患者：没做过手术。\n医生：胃口怎么样？会觉得吃的东西不怎么消化嘛？\n患者：吃东西都挺正常的，没有那种积食的感觉。\n医生：晚上睡眠质量怎么样？\n患者：睡眠质量挺好的，到时间就能正常睡觉。\n医生：大小便有什么异常没有？比如尿频、尿痛之类的情况？\n患者：没有。\n']
        ,speech
        ,label="医患对话样例"
    )
    recordTemplate.render()
    speech.render()
    submit_btn = gradio.Button("提交")
    outputs = gradio.TextArea(label="电子病历")
    submit_btn.click(
        fn = medicalRecordGenerating
        ,inputs=[recordTemplate,speech]
        ,outputs=outputs
    )
    
# app,local_url,share_url = demo.launch(server_name="192.168.1.131",server_port=7860, show_error=True)
demo.launch(server_name="192.168.31.95",server_port=7860, show_error=True)