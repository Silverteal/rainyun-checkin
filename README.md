# rainyun-checkin
automatically checkin rainyun through CI/CD
通过持续集成工具自动化进行雨云签到

## 使用方法
1.fork此存储库
2.转到仓库的Settings -> Secrets -> repository
3.添加RAINYUN_APIKEY，值为API密钥
4.大功告成！现在可以转到Actions，并手动触发工作流试试

## 特性
1.当RAINYUN_APIKEY为单个密钥时，工作流会检查签到成功与否，并在积分没有增加时使工作流失败
2.当RAINYUN_APIKEY是通过半角逗号分割的多个密钥时，工作流会依次签到，并只在所有密钥都没能使积分增加时使工作流失败
3.Github会自动冻结一些不活跃仓库（一般是60天）的Action
