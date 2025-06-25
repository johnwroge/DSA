"""
Job Sequencing Problem Templates
Applicable LeetCode Problems:
- 630. Course Schedule III
- 1235. Maximum Profit in Job Scheduling
- 1353. Maximum Number of Events That Can Be Attended
- 2050. Parallel Courses III
- 1834. Single-Threaded CPU
"""

import heapq
from collections import defaultdict

def job_sequencing_with_deadlines(jobs):
    """
    Classic job sequencing with deadlines and profits
    jobs: list of (job_id, deadline, profit) tuples
    Greedy: sort by profit (descending), schedule as late as possible
    Time: O(n²), Space: O(n)
    """
    if not jobs:
        return [], 0
    
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    # Find maximum deadline
    max_deadline = max(job[1] for job in jobs)
    
    # Initialize time slots (1-indexed)
    time_slots = [None] * (max_deadline + 1)
    
    total_profit = 0
    scheduled_jobs = []
    
    for job_id, deadline, profit in jobs:
        # Find latest available slot before or at deadline
        for slot in range(min(deadline, max_deadline), 0, -1):
            if time_slots[slot] is None:
                time_slots[slot] = job_id
                total_profit += profit
                scheduled_jobs.append((job_id, slot, profit))
                break
    
    return scheduled_jobs, total_profit

def job_sequencing_union_find(jobs):
    """
    Optimized job sequencing using Union-Find
    Time: O(n log n), Space: O(n)
    """
    if not jobs:
        return [], 0
    
    jobs.sort(key=lambda x: x[2], reverse=True)  # Sort by profit descending
    max_deadline = max(job[1] for job in jobs)
    
    # Union-Find to track next available slot
    parent = list(range(max_deadline + 2))  # Extra slot for overflow
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        parent[find(x)] = find(y)
    
    total_profit = 0
    scheduled_jobs = []
    
    for job_id, deadline, profit in jobs:
        available_slot = find(min(deadline, max_deadline))
        
        if available_slot > 0:
            total_profit += profit
            scheduled_jobs.append((job_id, available_slot, profit))
            union(available_slot, available_slot - 1)
    
    return scheduled_jobs, total_profit

def maximum_profit_job_scheduling(start_time, end_time, profit):
    """
    LeetCode 1235: Maximum Profit in Job Scheduling
    Dynamic programming with binary search
    Time: O(n log n), Space: O(n)
    """
    if not start_time:
        return 0
    
    jobs = list(zip(start_time, end_time, profit))
    jobs.sort(key=lambda x: x[1])  # Sort by end time
    
    n = len(jobs)
    dp = [0] * n
    dp[0] = jobs[0][2]  # First job's profit
    
    def find_latest_non_overlapping(i):
        """Binary search for latest job that doesn't overlap with job i"""
        left, right = 0, i - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            if jobs[mid][1] <= jobs[i][0]:  # No overlap
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    for i in range(1, n):
        # Option 1: Don't include current job
        exclude_profit = dp[i - 1]
        
        # Option 2: Include current job
        include_profit = jobs[i][2]
        latest_compatible = find_latest_non_overlapping(i)
        if latest_compatible >= 0:
            include_profit += dp[latest_compatible]
        
        dp[i] = max(exclude_profit, include_profit)
    
    return dp[n - 1]

def course_schedule_iii(courses):
    """
    LeetCode 630: Course Schedule III
    Maximum courses that can be taken within their deadlines
    Time: O(n log n), Space: O(n)
    """
    if not courses:
        return 0
    
    # Sort by deadline
    courses.sort(key=lambda x: x[1])
    
    max_heap = []  # Store negative durations (for max heap simulation)
    current_time = 0
    
    for duration, deadline in courses:
        current_time += duration
        heapq.heappush(max_heap, -duration)
        
        # If deadline exceeded, remove longest course taken so far
        if current_time > deadline:
            longest_duration = -heapq.heappop(max_heap)
            current_time -= longest_duration
    
    return len(max_heap)

def single_threaded_cpu(tasks):
    """
    LeetCode 1834: Single-Threaded CPU
    Process tasks in optimal order (shortest processing time first when CPU idle)
    Time: O(n log n), Space: O(n)
    """
    if not tasks:
        return []
    
    # Add indices to tasks and sort by enqueue time
    indexed_tasks = [(tasks[i][0], tasks[i][1], i) for i in range(len(tasks))]
    indexed_tasks.sort()
    
    result = []
    min_heap = []  # (processing_time, index)
    current_time = 0
    task_idx = 0
    
    while task_idx < len(indexed_tasks) or min_heap:
        # If CPU is idle and no tasks in queue, jump to next task
        if not min_heap and task_idx < len(indexed_tasks):
            current_time = max(current_time, indexed_tasks[task_idx][0])
        
        # Add all available tasks to queue
        while task_idx < len(indexed_tasks) and indexed_tasks[task_idx][0] <= current_time:
            enqueue_time, processing_time, original_idx = indexed_tasks[task_idx]
            heapq.heappush(min_heap, (processing_time, original_idx))
            task_idx += 1
        
        # Process next task
        if min_heap:
            processing_time, original_idx = heapq.heappop(min_heap)
            result.append(original_idx)
            current_time += processing_time
    
    return result

def minimize_maximum_lateness(jobs):
    """
    Minimize maximum lateness of jobs
    jobs: list of (processing_time, deadline) tuples
    Greedy: Earliest Deadline First (EDF)
    """
    if not jobs:
        return 0, []
    
    # Sort by deadline
    indexed_jobs = [(jobs[i], i) for i in range(len(jobs))]
    indexed_jobs.sort(key=lambda x: x[0][1])
    
    schedule = []
    current_time = 0
    max_lateness = 0
    
    for (processing_time, deadline), original_idx in indexed_jobs:
        start_time = current_time
        finish_time = current_time + processing_time
        lateness = max(0, finish_time - deadline)
        
        max_lateness = max(max_lateness, lateness)
        
        schedule.append({
            'job_id': original_idx,
            'start': start_time,
            'finish': finish_time,
            'deadline': deadline,
            'lateness': lateness
        })
        
        current_time = finish_time
    
    return max_lateness, schedule

def weighted_shortest_processing_time(jobs):
    """
    Minimize weighted completion time
    jobs: list of (processing_time, weight) tuples
    Greedy: sort by weight/processing_time ratio (descending)
    """
    if not jobs:
        return 0, []
    
    # Sort by weight/processing_time ratio in descending order
    indexed_jobs = [(jobs[i], i) for i in range(len(jobs))]
    indexed_jobs.sort(key=lambda x: x[0][1] / x[0][0], reverse=True)
    
    schedule = []
    current_time = 0
    total_weighted_completion = 0
    
    for (processing_time, weight), original_idx in indexed_jobs:
        current_time += processing_time
        weighted_completion = weight * current_time
        total_weighted_completion += weighted_completion
        
        schedule.append({
            'job_id': original_idx,
            'start': current_time - processing_time,
            'finish': current_time,
            'weight': weight,
            'weighted_completion': weighted_completion
        })
    
    return total_weighted_completion, schedule

def parallel_job_scheduling(jobs, num_machines):
    """
    Schedule jobs on multiple machines to minimize makespan
    jobs: list of processing times
    Greedy: assign job to machine with earliest finish time
    """
    if not jobs or num_machines <= 0:
        return []
    
    # Min heap: (finish_time, machine_id)
    machines = [(0, i) for i in range(num_machines)]
    heapq.heapify(machines)
    
    schedule = [[] for _ in range(num_machines)]
    
    for job_idx, processing_time in enumerate(jobs):
        # Get machine with earliest finish time
        earliest_finish, machine_id = heapq.heappop(machines)
        
        # Schedule job on this machine
        start_time = earliest_finish
        finish_time = start_time + processing_time
        
        schedule[machine_id].append({
            'job_id': job_idx,
            'start': start_time,
            'finish': finish_time,
            'processing_time': processing_time
        })
        
        # Update machine's finish time
        heapq.heappush(machines, (finish_time, machine_id))
    
    return schedule

def job_shop_scheduling_simple(jobs):
    """
    Simple job shop scheduling (each job has sequence of operations)
    jobs: list of [(machine_id, processing_time), ...] for each job
    Returns schedule for each machine
    """
    if not jobs:
        return {}
    
    machine_schedules = defaultdict(list)
    job_completion_times = [0] * len(jobs)
    machine_available_times = defaultdict(int)
    
    for job_id, operations in enumerate(jobs):
        current_job_time = job_completion_times[job_id]
        
        for machine_id, processing_time in operations:
            # Start time is max of job's current time and machine's available time
            start_time = max(current_job_time, machine_available_times[machine_id])
            finish_time = start_time + processing_time
            
            machine_schedules[machine_id].append({
                'job_id': job_id,
                'start': start_time,
                'finish': finish_time,
                'processing_time': processing_time
            })
            
            # Update times
            current_job_time = finish_time
            machine_available_times[machine_id] = finish_time
        
        job_completion_times[job_id] = current_job_time
    
    return dict(machine_schedules)

def priority_job_scheduling(jobs):
    """
    Schedule jobs with priorities (higher priority = higher value)
    jobs: list of (processing_time, priority, deadline) tuples
    """
    if not jobs:
        return []
    
    # Sort by priority (descending), then by deadline (ascending)
    indexed_jobs = [(jobs[i], i) for i in range(len(jobs))]
    indexed_jobs.sort(key=lambda x: (-x[0][1], x[0][2]))
    
    schedule = []
    current_time = 0
    
    for (processing_time, priority, deadline), original_idx in indexed_jobs:
        start_time = current_time
        finish_time = current_time + processing_time
        is_late = finish_time > deadline
        
        schedule.append({
            'job_id': original_idx,
            'start': start_time,
            'finish': finish_time,
            'deadline': deadline,
            'priority': priority,
            'is_late': is_late
        })
        
        current_time = finish_time
    
    return schedule