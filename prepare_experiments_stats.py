import os, time
from typing import IO


path_domain = 'domain/blocky_game.pddl'
problems_dir_path = 'problems/'
problems_name_prefix = 'problem-experiment'
stats_file_name = 'stats.txt'

plan_out_name = 'plan.out'
downward_command = \
    '~/downward/fast-downward.py --search-time-limit 10m --plan-file {} {} {} --evaluator "hff=ff()" --evaluator "hcea=cea()" --search "lazy_greedy([hff, hcea], preferred=[hff, hcea])" > solver_output.txt'

def run_downward(domain_path: str, problem_path: str, plan_out_path: str) -> tuple[float, int]:
    command = downward_command.format(plan_out_path, domain_path, problem_path)

    if os.path.exists(plan_out_path):
        os.remove(plan_out_path)

    start_time = time.monotonic()
    os.system(command)
    end_time = time.monotonic()

    if not os.path.exists(plan_out_path):
        plan_length = -1
    else:
        with open(plan_out_path, 'r') as file:
            plan_length = len(file.readlines()) - 1

    return end_time - start_time, plan_length

def append_stats_line(domain_path: str, problem_path: str, plan_out_path: str,
                      stats_file: IO, previous_stats: dict[str, tuple[float, int]]):
    if problem_path in previous_stats:
        planning_time, plan_length = previous_stats[problem_path]
        stats_line = f'{problem_path},{planning_time},{plan_length}\n'
        stats_file.write(stats_line)
        return

    print(f'Running experiment for problem: {problem_path}')
    planning_time, plan_length = run_downward(domain_path, problem_path, plan_out_path)
    stats_line = f'{problem_path},{planning_time},{plan_length}\n'
    stats_file.write(stats_line)

def read_previous_stats(stats_file_path: str) -> dict[str, tuple[float, int]]:
    stats = {}

    if not os.path.exists(stats_file_path):
        return stats

    with open(stats_file_path, 'r') as stats_file:
        stats_file.readline()
        for line in stats_file:
            problem_name, planning_time, plan_length = line.strip().split(',')
            stats[problem_name] = float(planning_time), int(plan_length)
    return stats

def run_experiments():
    previous_stats = read_previous_stats(stats_file_name)

    with open(stats_file_name, 'w+') as stats_file:
        header = 'problem_name,planning_time,plan_length\n'
        stats_file.write(header)

        main_problems = \
            [problem_file for problem_file in os.listdir(problems_dir_path)
             if problem_file.startswith(problems_name_prefix) and problem_file.endswith('.pddl')]
        main_problems_len = len(main_problems)

        for i, problem_file in enumerate(sorted(main_problems, key=lambda x: (len(x), x))):
            problem_name_without_extension = os.path.splitext(problem_file)[0]
            subproblem_dir_path = os.path.join(problems_dir_path, problem_name_without_extension)

            problem_path = os.path.join(problems_dir_path, problem_file)
            subproblem_dir_files = os.listdir(subproblem_dir_path)

            print(f"Running experiment for problem set ({i+1}/{main_problems_len}): ", problem_name_without_extension)

            for subproblem_file in subproblem_dir_files:
                subproblem_path = os.path.join(subproblem_dir_path, subproblem_file)
                append_stats_line(path_domain, subproblem_path, plan_out_name, stats_file, previous_stats)
            append_stats_line(path_domain, problem_path, plan_out_name, stats_file, previous_stats)

            stats_file.flush()


print('Running experiments...')
run_experiments()
print('Experiments finished!')
