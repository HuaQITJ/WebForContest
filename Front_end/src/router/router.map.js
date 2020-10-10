const routes = [
  // 用户信息
  {
    path: "/user",
    hideInMenu: true,
    component: () =>
      import(/* webpackChunkName: "layout" */ "../layouts/UserLayout.vue"),
    children: [
      {
        path: "/user",
        redirect: "/user/login"
      },
      {
        path: "/user/login",
        name: "login",
        component: () =>
          import(/* webpackChunkName: "user" */ "../views/user/Login.vue")
      }
    ]
  },
  // main
  {
    path: "/",
    component: () =>
      import(/* webpackChunkName: "layout" */ "../layouts/BasicLayout.vue"),
    children: [
      {
        path: "/",
        redirect: "/dashboard"
      },
      {
        path: "/dashboard",
        meta: { icon: "icon-shezhi", title: "数据看台" },
        name: "dashboard",
        component: () =>
          import(
            /* webpackChunkName: "dataDashboard" */ "../views/dataDashboard/Dashboard.vue"
          )
      },
      {
        path: "/work-dashboard",
        name: "work-dashboard",
        meta: { icon: "icon-gongzuo", title: "工作中台" },
        component: { render: h => h("router-view") },
        children: [
          {
            path: "/dashboard/authorization",
            name: "authorization",
            meta: { title: "我授权的B站号" },
            component: () =>
              import(
                /* webpackChunkName: "dashboard" */ "../views/workDashboard/Authorization .vue"
              )
          },
          {
            path: "/dashboard/attention",
            name: "attention",
            meta: { title: "我关注的UP主" },
            component: () =>
              import(
                /* webpackChunkName: "dashboard" */ "../views/workDashboard/Attention.vue"
              )
          },
          {
            path: "/dashboard/throw",
            name: "throw",
            meta: { title: "我投放的UP主" },
            component: () =>
              import(
                /* webpackChunkName: "dashboard" */ "../views/workDashboard/Throw.vue"
              )
          }
        ]
      },
      {
        path: "/hotBoard",
        name: "hotBoard",
        meta: { icon: "icon-yushouhuore", title: "火热看板" },
        component: { render: h => h("router-view") },
        children: [
          {
            path: "/hotBoard/hot-focus",
            name: "hot-focus",
            meta: { title: "火热看点" },
            component: () =>
              import(
                /* webpackChunkName: "HotFocus" */ "../views/hotBoard/HotFocus.vue"
              )
          }
        ]
      },
      {
        path: "/dataAdviser",
        name: "dataAdviser",
        meta: { icon: "icon-shuju", title: "数据参谋" },
        component: { render: h => h("router-view") },
        children: [
          {
            path: "/dataAdviser/hotList",
            name: "hotList",
            meta: { title: "站内热榜分析" },
            component: () =>
              import(
                /* webpackChunkName: "form" */ "../views/dataAdviser/HotList.vue"
              )
          },
          {
            path: "/dataAdviser/flowmeter",
            name: "flowmeter",
            meta: { title: "分区流量分析" },
            component: () =>
              import(
                /* webpackChunkName: "form" */ "../views/dataAdviser/Flowmeter.vue"
              )
          }
        ]
      }
    ]
  },
  {
    path: "*",
    hideInMenu: true,
    component: () =>
      import(/* webpackChunkName: "404" */ "../views/exception/404.vue")
  }
];

export default routes;
