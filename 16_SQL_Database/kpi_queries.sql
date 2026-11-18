-- KPI: 01_total_users
SELECT COUNT(DISTINCT user_id) AS total_users FROM users;

-- KPI: 02_active_users
SELECT COUNT(*) AS active_users, ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM users), 2) AS pct_of_users FROM users WHERE account_status = 'Active';

-- KPI: 03_onboarding_completion_rate
SELECT ROUND(100.0 * SUM(CASE WHEN onboarding_status = 'Completed' THEN 1 ELSE 0 END) / COUNT(*), 2) AS onboarding_completion_pct FROM users;

-- KPI: 04_users_by_acquisition_source
SELECT acquisition_source, COUNT(*) AS users FROM users GROUP BY acquisition_source ORDER BY users DESC;

-- KPI: 05_session_summary
SELECT COUNT(*) AS total_sessions, ROUND(AVG(session_duration_seconds), 1) AS avg_duration_sec, ROUND(1.0 * COUNT(*) / COUNT(DISTINCT user_id), 2) AS sessions_per_user FROM sessions;

-- KPI: 06_avg_daily_active_users
SELECT ROUND(AVG(dau), 1) AS avg_dau FROM (SELECT activity_date, COUNT(DISTINCT user_id) AS dau FROM daily_activity GROUP BY activity_date);

-- KPI: 07_returning_users
SELECT COUNT(*) AS returning_users FROM (SELECT user_id FROM daily_activity GROUP BY user_id HAVING COUNT(DISTINCT activity_date) >= 2);

-- KPI: 08_task_status_breakdown
SELECT task_status, COUNT(*) AS tasks, ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM task_activity), 2) AS pct FROM task_activity GROUP BY task_status ORDER BY tasks DESC;

-- KPI: 09_task_completion_by_category
SELECT task_category, COUNT(*) AS tasks, ROUND(100.0 * SUM(CASE WHEN task_status = 'Completed' THEN 1 ELSE 0 END) / COUNT(*), 2) AS completion_pct FROM task_activity GROUP BY task_category ORDER BY completion_pct DESC;

-- KPI: 10_reward_credit_rate
SELECT SUM(CASE WHEN task_status = 'Completed' THEN 1 ELSE 0 END) AS completed_tasks, SUM(CASE WHEN reward_status = 'Credited' THEN 1 ELSE 0 END) AS credited_rewards, ROUND(100.0 * SUM(CASE WHEN reward_status = 'Credited' THEN 1 ELSE 0 END) / SUM(CASE WHEN task_status = 'Completed' THEN 1 ELSE 0 END), 2) AS credit_rate_pct FROM task_activity;

-- KPI: 11_top_features_by_events
SELECT feature_name, COUNT(*) AS events, COUNT(DISTINCT user_id) AS unique_users FROM feature_events GROUP BY feature_name ORDER BY events DESC LIMIT 10;

-- KPI: 12_milestones_by_type
SELECT milestone_type, COUNT(*) AS milestones, COUNT(DISTINCT user_id) AS users FROM milestones GROUP BY milestone_type ORDER BY milestones DESC;
