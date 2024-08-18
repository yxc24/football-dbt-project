WITH team_stats AS (
    SELECT
        home_team AS team,
        COUNT(*) AS games_played,
        SUM(CASE WHEN home_goals > away_goals THEN 1 ELSE 0 END) AS wins,
        SUM(CASE WHEN home_goals = away_goals THEN 1 ELSE 0 END) AS draws,
        SUM(CASE WHEN home_goals < away_goals THEN 1 ELSE 0 END) AS losses,
        SUM(home_goals) AS goals_for,
        SUM(away_goals) AS goals_against
    FROM {{ source('football_data', 'matches') }}
    GROUP BY home_team

    UNION ALL

    SELECT
        away_team AS team,
        COUNT(*) AS games_played,
        SUM(CASE WHEN away_goals > home_goals THEN 1 ELSE 0 END) AS wins,
        SUM(CASE WHEN away_goals = home_goals THEN 1 ELSE 0 END) AS draws,
        SUM(CASE WHEN away_goals < home_goals THEN 1 ELSE 0 END) AS losses,
        SUM(away_goals) AS goals_for,
        SUM(home_goals) AS goals_against
    FROM {{ source('football_data', 'matches') }}
    GROUP BY away_team
)

SELECT
    team,
    SUM(games_played) AS total_games,
    SUM(wins) AS total_wins,
    SUM(draws) AS total_draws,
    SUM(losses) AS total_losses,
    SUM(goals_for) AS total_goals_for,
    SUM(goals_against) AS total_goals_against,
    SUM(wins) * 3 + SUM(draws) AS points
FROM team_stats
GROUP BY team
ORDER BY points DESC
