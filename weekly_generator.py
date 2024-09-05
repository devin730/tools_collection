import datetime

def generate_weekly_report(week_start, week_end, tasks):
    # 生成周报标题
    report_title = f"## 周报：{week_start.strftime('%Y-%m-%d')} 至 {week_end.strftime('%Y-%m-%d')}\n"

    # 生成任务部分
    report_tasks = "### 本周完成的任务\n"
    for task in tasks:
        report_tasks += f"- {task}\n"

    # 生成总结部分
    report_summary = "### 本周总结\n"
    report_summary += "本周的工作进展顺利，期待下周的挑战！\n"

    # 组合周报
    report = report_title + report_tasks + report_summary

    return report

def main():
    # 获取当前日期
    today = datetime.date.today()

    # 计算本周的开始和结束日期
    week_start = today - datetime.timedelta(days=today.weekday())  # 本周一
    week_end = week_start + datetime.timedelta(days=6)  # 本周日

    # 输入本周完成的任务
    tasks = []
    print("请输入本周完成的任务（输入'结束'以完成输入）：")
    while True:
        task = input("任务：")
        if task.lower() == '结束':
            break
        tasks.append(task)

    # 生成周报
    report = generate_weekly_report(week_start, week_end, tasks)

    # 保存周报到文件
    with open('weekly_report.md', 'w', encoding='utf-8') as f:
        f.write(report)

    print("周报已成功生成并保存为 'weekly_report.md'。")

if __name__ == "__main__":
    main()