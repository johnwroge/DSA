import pandas as pd

def assign_tasks(tasks_file, candidates_file, output_file):
    tasks = pd.read_csv(tasks_file)
    candidates = pd.read_csv(candidates_file)
    output = pd.DataFrame(columns=['ticket', 'assignee', 'hours'])

    for _, task in tasks.iterrows():
        group_candidates = candidates[candidates['group'] == task['group']]

        if not group_candidates.empty:
            assignee = group_candidates.loc[group_candidates['hours'].idxmax(), 'candidate']
            assigned_hours = min(task['estimation'], group_candidates.loc[group_candidates['candidate'] == assignee, 'hours'].values[0])

            output = output.append({
                'ticket': task['ticketNumber'],
                'assignee': assignee,
                'hours': assigned_hours
            }, ignore_index=True)

            candidates.loc[candidates['candidate'] == assignee, 'hours'] -= assigned_hours

    output.to_csv(output_file, index=False)

# Example usage
assign_tasks('tasks.csv', 'candidates.csv', 'assigned_tasks.csv')
