from server.routers import staff, users_staff, users_viewer, viewers, tv_channels, schedules, equipment_sets, staff_teams, times, shows

routs = (users_staff.user_staff_router, staff.staff_router, users_viewer.user_viewer_router, viewers.viewers_router,
         tv_channels.channel_router, equipment_sets.equipment_router, staff_teams.staff_teams_router,
         times.times_router, equipment_sets.equipment_sets_router, equipment_sets.equipment_names_router,
         schedules.schedules_id_router, schedules.schedules_router, shows.shows_router)
