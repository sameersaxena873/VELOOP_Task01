# SQL Queries Explained (Hinglish)

SIMULATED — CREATED FOR ANALYTICAL TESTING. Not actual VELOOP data.

> Note: Ye file pehle ki original file ki jagah naye sire se likhi gayi hai. Original content wapas nahi mila.

---

## 1. Basic SQL Keywords

- **SELECT:** Kaun se columns dikhane hain.
- **FROM:** Kis table se data lena hai.
- **WHERE:** Sirf wahi rows jo condition match karein.
- **GROUP BY:** Ek category ke hisaab se rows ki gathri banana.
- **COUNT(\*):** Rows ginna.
- **COUNT(DISTINCT x):** Alag-alag values ginna.
- **ORDER BY ... DESC:** Bade se chhota sort karna.
- **HAVING:** GROUP BY ke baad condition lagana.
- **CASE WHEN:** SQL ka if-else, percentage nikalne ke liye.
- **ROUND(x, 2):** Number ko 2 decimal tak round karna.

---

## 2. KPI Queries

### 1. total_users
Alag user_id ginta hai, taaki same user do baar na gine jaaye.
```sql
SELECT COUNT(DISTINCT user_id) FROM users;
```

### 2. active_users
Active account wale users aur unka percentage.
```sql
SELECT COUNT(*) FROM users WHERE account_status = 'Active';
```

### 3. onboarding_completion_rate
Completed onboarding wale users / total users * 100.
```sql
SELECT ROUND(100.0 * SUM(onboarding_status = 'Completed') / COUNT(*), 2) FROM users;
```

### 4. users_by_acquisition_source
Har source se kitne users aaye.
```sql
SELECT acquisition_source, COUNT(*) AS users
FROM users
GROUP BY 1
ORDER BY 2 DESC;
```

### 5. session_summary
Total sessions, average duration, aur sessions per user.
```sql
SELECT COUNT(*) FROM sessions;
```

### 6. avg_daily_active_users
Har date ke unique users ka average.

### 7. returning_users
2 ya zyada alag dino par active users.

### 8. task_status_breakdown
Completed, Failed, Abandoned, Pending ki count aur percentage.
```sql
SELECT task_status, COUNT(*),
       ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM task_activity), 2) AS pct
FROM task_activity
GROUP BY task_status
ORDER BY 2 DESC;
```

---

## 3. Pending

Build script mein "12 KPI queries" likha gaya tha, lekin 8 hi listed hain. Baaki 4 KPIs (jaise reward credit rate, top features, milestones) ka content baad mein add karna hai, aur tab tak ye file adhoori hai.
